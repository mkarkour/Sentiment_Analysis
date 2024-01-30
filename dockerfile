# Utiliser l'image de base Python
FROM python:3.9

# Créer un répertoire d'application dans l'image
WORKDIR /app

# Copier les fichiers du projet dans l'image
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port nécessaire pour Streamlit (par défaut 8501)
EXPOSE 8501

# Commande à exécuter lorsque le conteneur démarre
CMD ["python","-m","streamlit", "run", "src/main.py"]
