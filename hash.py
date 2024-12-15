import yaml
from streamlit_authenticator import Hasher

# Charger le fichier YAML
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Afficher les informations avant le hachage
print("Avant hachage des mots de passe:")
print(config['credentials'])

# Hacher les mots de passe
hashed_credentials = Hasher.hash_passwords(config['credentials'])

# Vérification de la structure du résultat
if 'usernames' in hashed_credentials:
    print("\nAprès hachage des mots de passe:")
    print(hashed_credentials['usernames'])
else:
    print("Erreur : la structure des credentials hachés n'est pas correcte.")

# Mettre à jour le fichier YAML avec les mots de passe hachés
with open("config_hashed.yaml", "w") as file:
    yaml.dump(hashed_credentials, file)

print("\nLes mots de passe ont été hachés et sauvegardés dans 'config_hashed.yaml'.")
