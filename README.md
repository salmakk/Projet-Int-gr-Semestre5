Projet Intégré - Automatisation de Gestion des VMs avec vSphere
Description du projet
Ce projet vise à automatiser le provisionnement et la gestion des machines virtuelles (VMs) en utilisant VMware vSphere. Grâce à une interface utilisateur simple, les utilisateurs peuvent s'authentifier, sélectionner des modèles de VM et suivre le statut du provisionnement.

Technologies utilisées
Frontend : HTML, CSS, JavaScript <img src="![image](https://github.com/user-attachments/assets/39fbe63e-ed2f-4544-ae62-e80712f9892b)" width="300">
Backend : Python (Flask) <img src="![image](https://github.com/user-attachments/assets/39fbe63e-ed2f-4544-ae62-e80712f9892b)" width="50">
Base de données : MongoDB <img src="![image](https://github.com/user-attachments/assets/39fbe63e-ed2f-4544-ae62-e80712f9892b)" width="50">
Virtualisation : VMware vSphere (vCenter, ESXi) <img src="![image](https://github.com/user-attachments/assets/39fbe63e-ed2f-4544-ae62-e80712f9892b)" width="50">
1️⃣ Architecture du Projet
📌 Diagramme de l’architecture globale
<img src="![image](https://github.com/user-attachments/assets/39fbe63e-ed2f-4544-ae62-e80712f9892b)" width="50">
2️⃣ Interaction Frontend-Backend
📌 Schéma d’interaction
<img src="![image](https://github.com/user-attachments/assets/cc53d10e-1808-48fc-be52-cdb0a24a7f09)
" width="50">
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
