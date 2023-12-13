import hashlib # Module pour hasher le mot de passe
import json # Module pour enregistrer les mots de passe dans un fichier

caracteres_special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"] # Liste des caractères spéciaux

def caracteres_speciaux(mot_de_passe): # Fonction pour vérifier si le mot de passe contient un caractère spécial
    global caracteres_special # Rend la variable globale
    for i in caracteres_special: # Boucle pour vérifier si le mot de passe contient un caractère spécial
        if i in mot_de_passe: # Si le mot de passe contient un caractère spécial
            return True # Retourne True
    return False # Retourne False

def hash_mot_de_passe(mot_de_passe): # Fonction pour hasher le mot de passe
    hashed_password = hashlib.sha256(mot_de_passe.encode()).hexdigest() # Hash le mot de passe
    return hashed_password # Retourne le mot de passe hashé

def enregistrer_mot_de_passe(mot_de_passe): # Fonction pour enregistrer le mot de passe
    try: # Essaie d'ouvrir le fichier
        with open("mots_de_passe.json", "r") as file: # Ouvre le fichier
            mots_de_passe_existants = json.load(file) # Charge le fichier
    except (FileNotFoundError, json.JSONDecodeError): # Si le fichier n'existe pas ou est vide
        mots_de_passe_existants = [] # Crée une liste vide

    mots_de_passe_existants.append(hash_mot_de_passe(mot_de_passe)) # Ajoute le mot de passe hashé à la liste

    with open("mots_de_passe.json", "w") as file: # Ouvre le fichier
        json.dump(mots_de_passe_existants, file) # Enregistre la liste dans le fichier

def afficher_mots_de_passe(): # Fonction pour afficher les mots de passe
    try: # Essaie d'ouvrir le fichier
        with open("mots_de_passe.json", "r") as file: # Ouvre le fichier
            mots_de_passe_existants = json.load(file) # Charge le fichier
        print("Mots de passe enregistrés :") # Affiche les mots de passe
        for i, hashed_password in enumerate(mots_de_passe_existants, start=1): # Boucle pour afficher les mots de passe
            print(f"{i}. {hashed_password}") # Affiche les mots de passe
    except (FileNotFoundError, json.JSONDecodeError): # Si le fichier n'existe pas ou est vide
        print("Aucun mot de passe enregistré.") # Affiche qu'il n'y a pas de mot de passe enregistré

def programme(): # Fonction pour le programme
    while True: # Boucle pour le programme
        print("1. Ajouter un nouveau mot de passe") # Affiche les options
        print("2. Afficher les mots de passe enregistrés") # Affiche les options
        print("3. Quitter") # Affiche les options
        choix = input("Choisissez une option (1/2/3) : ") # Demande à l'utilisateur de choisir une option

        if choix == "1": # Si l'utilisateur choisit l'option 1
            mot_de_passe = input("Entrez votre mot de passe : ") # Demande à l'utilisateur d'entrer un mot de passe
            if len(mot_de_passe) < 8: # Si le mot de passe est trop court
                print("Le mot de passe est trop court, il doit contenir au moins 8 caractères.") # Affiche que le mot de passe est trop court
            elif mot_de_passe.isalpha(): # Si le mot de passe contient que des lettres
                print("Le mot de passe contient que des lettres.") # Affiche que le mot de passe contient que des lettres
            elif mot_de_passe.isupper(): # Si le mot de passe contient que des majuscules
                print("Le mot de passe contient que des majuscules.") # Affiche que le mot de passe contient que des majuscules
            elif mot_de_passe.islower(): # Si le mot de passe contient que des minuscules
                print("Le mot de passe contient que des minuscules.") # Affiche que le mot de passe contient que des minuscules
            elif mot_de_passe.isdigit(): # Si le mot de passe contient que des chiffres
                print("Le mot de passe contient que des chiffres.") # Affiche que le mot de passe contient que des chiffres
            elif not caracteres_speciaux(mot_de_passe): # Si le mot de passe ne contient pas de caractère spécial
                print("Votre mot de passe doit contenir au moins un caractère spécial.") # Affiche que le mot de passe ne contient pas de caractère spécial
            else: # Si le mot de passe est valide
                enregistrer_mot_de_passe(mot_de_passe) # Enregistre le mot de passe
                print("Votre mot de passe est validé et a été enregistré.") # Affiche que le mot de passe est validé et a été enregistré
        elif choix == "2": # Si l'utilisateur choisit l'option 2
            afficher_mots_de_passe() # Affiche les mots de passe
        elif choix == "3": # Si l'utilisateur choisit l'option 3
            print("Programme terminé.") # Affiche que le programme est terminé
            break # Arrête la boucle
        else: # Si l'utilisateur choisit une option invalide
            print("Choix invalide. Veuillez choisir 1, 2 ou 3.") # Affiche que l'option est invalide

if __name__ == "__main__": # Si le fichier est exécuté directement
    programme() # Exécute le programme