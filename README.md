Projet Intégré - Automatisation de Gestion des VMs avec vSphere
Description du projet
Ce projet vise à automatiser le provisionnement et la gestion des machines virtuelles (VMs) en utilisant VMware vSphere. Grâce à une interface utilisateur simple, les utilisateurs peuvent s'authentifier, sélectionner des modèles de VM et suivre le statut du provisionnement.

Technologies utilisées
Frontend : HTML, CSS, JavaScript
Backend : Python (Flask) 
Base de données : MongoDB 
Virtualisation : VMware vSphere (vCenter, ESXi)
1️⃣ Architecture du Projet
📌 Diagramme de l’architecture globale
![image](https://github.com/user-attachments/assets/a6e79a18-c7dd-49ed-b2d1-ac120c3a2020)
2️⃣ Interaction Frontend-Backend
📌 Schéma d’interaction
![Capture d'écran 2025-02-22 132106](https://github.com/user-attachments/assets/63d4c7f4-959d-4f9e-b45e-92ffca51b330)
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
