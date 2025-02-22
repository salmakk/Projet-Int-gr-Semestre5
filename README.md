Projet Intégré - Automatisation de Gestion des VMs avec vSphere
Description du projet
Ce projet vise à automatiser le provisionnement et la gestion des machines virtuelles (VMs) en utilisant VMware vSphere. Grâce à une interface utilisateur simple, les utilisateurs peuvent s'authentifier, sélectionner des modèles de VM et suivre le statut du provisionnement.

Technologies utilisées
Frontend : HTML, CSS, JavaScript <img src="![image](https://github.com/user-attachments/assets/39fbe63e-ed2f-4544-ae62-e80712f9892b)" alt="Schéma d'architecture" width="100">
Backend : Python (Flask)
![image](https://github.com/user-attachments/assets/0335d262-65c4-4abf-bd7f-110423af471b)
Base de données : MongoDB
![image](https://github.com/user-attachments/assets/ab33fca2-e3ba-477a-9de5-2f3661792e3d)
Virtualisation : VMware vSphere (vCenter, ESXi)
![image](https://github.com/user-attachments/assets/ad774925-c8eb-4391-813a-6fad6bcd260e)
1️⃣ Architecture du Projet
📌 Diagramme de l’architecture globale
![image](https://github.com/user-attachments/assets/b9a5351a-dc57-40a7-ad51-4a0c08f39552)
2️⃣ Interaction Frontend-Backend
📌 Schéma d’interaction
![image](https://github.com/user-attachments/assets/d3008347-9ef0-4211-b231-7154091bd95a)
3️⃣ Installation et Configuration
📌 Prérequis
Avant de commencer, assure-toi d'avoir :
✅ Python 3.x installé
✅ MongoDB en service
✅ Un accès à un serveur VMware vSphere
✅ Node.js (pour le frontend)

#### 1️⃣ Configuration de la base de données MongoDB
Vérifie que MongoDB est en cours d'exécution sur `mongodb://localhost:27017`.

#### 2️⃣ Lancer le Backend
```bash
python app.py
```

#### 3️⃣ Installation et exécution du Frontend
```bash
cd ../frontend
npm install
npm start
```
5️⃣ Contribuer
Les contributions sont les bienvenues ! Pour proposer une modification :
Forke le projet
Crée une nouvelle branche
Apporte tes modifications
Fais une pull request :)
