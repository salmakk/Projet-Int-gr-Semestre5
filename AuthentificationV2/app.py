import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
from flask import jsonify
import subprocess
import ssl
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Connexion à MongoDB
# Remplacez l'URI de connexion avec celui obtenu dans MongoDB Compass ou votre MongoDB local.
client = MongoClient("mongodb://localhost:27017/")  # Connexion à MongoDB local
db = client.vmware_auth  # Nom de la base de données
users_collection = db.users  # Collection "users" dans la base de données
templatecol=db.templatecol
vmcol=db.vmcol
P@ssw0rd
# Ignorer les avertissements SSL pour vSphere
context = ssl._create_unverified_context()

# Configuration vSphere
vsphere_host = '10.40.60.5'
vsphere_user = 'Administrator@vsphere.local'
vsphere_password = 'Groupe@5'
datacenter_name = 'Groupe5-Datacenter'
datastore_name = 'DS5'
host_name = '10.40.51.5'
portgroup_name = 'Nouveau_Network_Port_Group'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = users_collection.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            session['user'] = user['email']
            session['nameus'] = user['name']
            flash('Connexion réussie!', 'success')
            return redirect(url_for('createvm'))
        else:
            flash('Email ou mot de passe incorrect.', 'danger')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        if users_collection.find_one({'email': email}):
            flash('Cet email est déjà enregistré.', 'danger')
        else:
            hashed_password = generate_password_hash(password)
            users_collection.insert_one({'name': name, 'email': email, 'password': hashed_password})
            flash('Inscription réussie! Veuillez vous connecter.', 'success')
            return redirect(url_for('login'))
    return render_template('signup.html')


import subprocess

@app.route('/connect', methods=['POST'])
def connect():
    vm_id = request.form.get('vm_id')
    if not vm_id:
        return "No VM selected.", 400

    selected_vm = vmcol.find_one({'_id': vm_id})
    if not selected_vm:
        return "VM not found.", 404

    # Détails de la VM
    vm_name = selected_vm.get('name')
    ip_address = selected_vm.get('ip_address')
    os_type = selected_vm.get('os')  # Vérifie si c'est Windows ou Linux

    if os_type.startswith('Windows'):
        # Commande RDP pour Windows
        rdp_command = f"mstsc /v:{ip_address}"
        try:
            subprocess.run(rdp_command, shell=True)
            return f"Connexion RDP lancée pour la VM '{vm_name}' (IP: {ip_address})."
        except Exception as e:
            return f"Erreur lors de l'exécution de RDP : {str(e)}", 500

    elif os_type.startswith('Linux'):
        # Commande SSH pour Linux
        ssh_command = f"ssh user@{ip_address}"  # Remplacez 'user' par l'utilisateur SSH par défaut
        return f"Pour vous connecter via SSH, exécutez cette commande dans votre terminal : {ssh_command}"

    else:
        return "Système d'exploitation non pris en charge pour la connexion.", 400


@app.route('/create', methods=['POST'])
def create_vm():
    template_id = request.form.get('template_id')
    new_vm_name = request.form.get('vm_name')
    template = templatecol.find_one({'_id': template_id})
    template_name = template['template_name']


    try:
        # Connexion à vSphere
        si = SmartConnect(host=vsphere_host, user=vsphere_user, pwd=vsphere_password, sslContext=context)
        print("Connexion réussie à vSphere")

        # Récupérer le Datacenter
        content = si.RetrieveContent()
        datacenter = next(dc for dc in content.rootFolder.childEntity if dc.name == datacenter_name)

        # Rechercher le modèle
        template = next((vm for vm in datacenter.vmFolder.childEntity if vm.name == template_name), None)
        if not template:
            return jsonify({'error': f"Modèle {template_name} introuvable."}), 404

        # Récupérer le Datastore et l'Hôte
        datastore = next(ds for ds in datacenter.datastoreFolder.childEntity if ds.name == datastore_name)
        host = next(h for h in datacenter.hostFolder.childEntity[0].host if h.name == host_name)

        # Configurer les spécifications de clonage
        relocate_spec = vim.vm.RelocateSpec()
        relocate_spec.host = host
        relocate_spec.datastore = datastore
        relocate_spec.pool = datacenter.hostFolder.childEntity[0].resourcePool

        # Ajouter une personnalisation pour activer RDP
        windows_custom_spec = vim.vm.customization.Specification()
        identity = vim.vm.customization.Sysprep()
        identity.userData = vim.vm.customization.UserData()
        identity.userData.computerName = vim.vm.customization.FixedName(name=new_vm_name)
        identity.userData.fullName = "Administrator"
        identity.userData.orgName = "Organization"
        identity.userData.productId = ""  # Laissez vide pour une clé générique
        identity.guiUnattended = vim.vm.customization.GuiUnattended()
        identity.guiUnattended.timeZone = 85  # Fuseau horaire (85 = UTC+1)
        identity.guiUnattended.autoLogon = True
        identity.guiUnattended.autoLogonCount = 1

        # Script PowerShell pour activer RDP
        identity.guiRunOnce = vim.vm.customization.GuiRunOnce()
        identity.guiRunOnce.commandList = [
            "powershell.exe -Command \"Set-ItemProperty -Path 'HKLM:\\System\\CurrentControlSet\\Control\\Terminal Server' -Name 'fDenyTSConnections' -Value 0\"",
            "powershell.exe -Command \"Enable-NetFirewallRule -DisplayGroup 'Remote Desktop'\""
        ]

        windows_custom_spec.identity = identity

        # Créer les spécifications de clonage avec personnalisation
        clone_spec = vim.vm.CloneSpec()
        clone_spec.location = relocate_spec
        clone_spec.powerOn = True
        clone_spec.customization = windows_custom_spec

        # Lancer le clonage
        task = template.Clone(folder=datacenter.vmFolder, name=new_vm_name, spec=clone_spec)
        print(f"Clonage de la VM '{new_vm_name}' en cours...")

        # Suivre l'état de la tâche avec progression
        while task.info.state == vim.TaskInfo.State.running:
            print("Progression :", task.info.progress)
            time.sleep(5)

        if task.info.state == vim.TaskInfo.State.success:
            # Récupérer l'adresse IP de la VM
            cloned_vm = next((vm for vm in datacenter.vmFolder.childEntity if vm.name == new_vm_name), None)
            ip_address = None
            if cloned_vm and cloned_vm.guest.net:
                for nic in cloned_vm.guest.net:
                    if nic.ipConfig and nic.ipConfig.ipAddress:
                        ip_address = nic.ipConfig.ipAddress[0].ipAddress
                        break

            if ip_address:
                # Enregistrer la VM dans MongoDB
                vmcol.insert_one({
                    'name': new_vm_name,
                    'ip_address': ip_address,
                    'creation_date': time.strftime('%Y-%m-%d %H:%M:%S'),
                })
                return jsonify({'message': f"VM '{new_vm_name}' créée avec succès.", 'ip_address': ip_address}), 201
            else:
                return jsonify({'error': "Impossible de récupérer l'adresse IP de la VM."}), 500

        else:
            return jsonify({'error': f"Échec du clonage : {task.info.error}"}), 500

    except Exception as e:
        return jsonify({'error': f"Erreur lors du clonage de la VM : {str(e)}"}), 500

    finally:
        Disconnect(si)
        print("Déconnexion de vSphere")


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Déconnexion réussie.', 'success')
    return redirect(url_for('home'))
@app.route('/createvm')
def createvm():
    vms = list(templatecol.find())
    return render_template('template.html', vms=vms,session=session)
@app.route('/vms')
def vms_list():

    user_vms = list(vmcol.find())

    return render_template('vms_list.html', user_vms=user_vms,session=session)

if __name__ == '__main__':
    app.run(debug=True)
