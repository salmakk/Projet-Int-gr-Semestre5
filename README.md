# Projet Intégré - Automatisation de Gestion des VMs avec vSphere

## Description du projet
Ce projet vise à automatiser le provisionnement et la gestion des machines virtuelles (VMs) en utilisant VMware vSphere. L'interface utilisateur permet aux utilisateurs de s'authentifier, de sélectionner des modèles de VM, de suivre le statut du provisionnement et de gérer leurs VMs de manière simple et intuitive.

Les principales fonctionnalités incluent :
- Authentification des utilisateurs
- Sélection de modèles de machines virtuelles
- Suivi du statut des VMs
- Gestion des erreurs et alertes en temps réel

## Technologies utilisées
- **Frontend** : HTML, CSS, JavaScript
- **Backend** : Python (Flask)
- **Base de données** : MongoDB
- **Virtualisation** : VMware vSphere (vCenter, ESXi)

## 1️⃣ Architecture du Projet

### Diagramme de l’architecture globale
Voici l'architecture globale du projet qui décrit l'interaction entre le frontend, le backend et les services de virtualisation :

![Architecture globale](https://github.com/user-attachments/assets/a6e79a18-c7dd-49ed-b2d1-ac120c3a2020)

### Description de l'architecture
- **Frontend** : L'interface utilisateur est construite avec HTML, CSS et JavaScript, permettant aux utilisateurs d'interagir avec le système.
- **Backend** : Le backend est développé en Python avec Flask, permettant de gérer les requêtes utilisateurs, l'authentification et l'interaction avec la base de données et VMware vSphere.
- **Base de données** : MongoDB est utilisé pour stocker les informations relatives aux utilisateurs, aux VMs et aux journaux de provisionnement.
- **VMware vSphere** : Nous utilisons VMware vSphere pour gérer la virtualisation, avec les composants vCenter et ESXi.

## 2️⃣ Installation et Configuration

### Prérequis
Avant de commencer l'installation, assure-toi d'avoir les éléments suivants configurés :
- **Python 3.x** : Télécharge et installe depuis [python.org](https://www.python.org/downloads/).
- **MongoDB** : Assure-toi que MongoDB est installé et en service sur `mongodb://localhost:27017`. Si nécessaire, tu peux installer MongoDB depuis [mongodb.com](https://www.mongodb.com/try/download/community).
- **VMware vSphere** : Un accès à un serveur VMware vSphere, notamment les services **vCenter** et **ESXi**.
- **Node.js** : Télécharge et installe la dernière version de Node.js depuis [nodejs.org](https://nodejs.org/).

### Étapes d'installation

#### 1️⃣ Configuration de la base de données MongoDB
MongoDB doit être en cours d'exécution sur l'URL suivante : `mongodb://localhost:27017`. Vérifie que ton instance est accessible.

#### 2️⃣ Lancer le Backend
Le backend est développé en Python avec Flask. Pour lancer l'application :
1. Clone le dépôt du projet :
   ```bash
   git clone https://github.com/salmakk/Projet-Int-gr-Semestre5.git
2. Lance le serveur Flask :
   ```bash
   python app.py
   
#### 3️⃣ Contribuer
Les contributions sont les bienvenues ! Si tu souhaites proposer une modification, voici les étapes à suivre :

1. **Fork le projet** sur GitHub en cliquant sur le bouton "Fork" en haut à droite de cette page.
   
2. **Clone ton fork localement** :
   ```bash
   git clone https://github.com/ton-nom-utilisateur/Projet-Int-gr-Semestre5.git
   
3. **Crée une nouvelle branche** :
   ```bash
   git checkout -b feature/ma-fonctionnalité
   
4. **Ajout Modifications** :
   ```bash
   git add .
   git commit -m "Ajoute une fonctionnalité XYZ"
   
5. **Pousse ta branche vers ton dépôt distant** :
   ```bash
   git push origin feature/ma-fonctionnalité
   
:) :) :)

