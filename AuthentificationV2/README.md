1. Clonez ou créez un répertoire pour l'application
Clonez le projet ou placez les fichiers dans un répertoire.


git clone <URL-du-dépot>
cd <dossier-de-l'application>


2. Installez les dépendances
Créez un environnement virtuel et installez les dépendances :


python -m venv venv

source venv/bin/activate  # Sous macOS/Linux

venv\Scripts\activate     # Sous Windows

pip install flask pymongo werkzeug


3. Configurez MongoDB
Installez MongoDB et démarrez-le. Assurez-vous que MongoDB fonctionne sur localhost:27017.

4. Exécutez l'application
Lancez l'application Flask :


python app.py
L'application sera accessible à l'adresse http://127.0.0.1:5000.