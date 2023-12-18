import hashlib
import json
import random
import string

caracteres_special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]

def caracteres_speciaux(mot_de_passe):
    global caracteres_special
    for i in caracteres_special:
        if i in mot_de_passe:
            return True
    return False

def hash_mot_de_passe(mot_de_passe):
    hashed_password = hashlib.sha256(mot_de_passe.encode()).hexdigest()
    return hashed_password

def generer_mot_de_passe():
    longueur_mot_de_passe = random.randint(10, 15)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur_mot_de_passe))
    return mot_de_passe

def enregistrer_mot_de_passe(mot_de_passe):
    try:
        with open("mots_de_passe.json", "r") as file:
            mots_de_passe_existants = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        mots_de_passe_existants = []

    hashed_password = hash_mot_de_passe(mot_de_passe)

    if hashed_password not in mots_de_passe_existants:
        mots_de_passe_existants.append(hashed_password)

        with open("mots_de_passe.json", "w") as file:
            json.dump(mots_de_passe_existants, file)

def afficher_mots_de_passe():
    try:
        with open("mots_de_passe.json", "r") as file:
            mots_de_passe_existants = json.load(file)
        print("Mots de passe enregistrés :")
        for i, hashed_password in enumerate(mots_de_passe_existants, start=1):
            print(f"{i}. {hashed_password}")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Aucun mot de passe enregistré.")

def programme():
    while True:
        print("1. Ajouter un nouveau mot de passe")
        print("2. Générer un mot de passe aléatoire")
        print("3. Afficher les mots de passe enregistrés")
        print("4. Quitter")
        choix = input("Choisissez une option (1/2/3/4) : ")

        if choix == "1":
            mot_de_passe = input("Entrez votre mot de passe : ")
            if len(mot_de_passe) < 8:
                print("Le mot de passe est trop court, il doit contenir au moins 8 caractères.")
            elif mot_de_passe.isalpha():
                print("Le mot de passe contient que des lettres.")
            elif mot_de_passe.isupper():
                print("Le mot de passe contient que des majuscules.")
            elif mot_de_passe.islower():
                print("Le mot de passe contient que des minuscules.")
            elif mot_de_passe.isdigit():
                print("Le mot de passe contient que des chiffres.")
            elif not caracteres_speciaux(mot_de_passe):
                print("Votre mot de passe doit contenir au moins un caractère spécial.")
            else:
                enregistrer_mot_de_passe(mot_de_passe)
                print("Votre mot de passe est validé et a été enregistré.")
        elif choix == "2":
            mot_de_passe_aleatoire = generer_mot_de_passe()
            print(f"Mot de passe aléatoire généré : {mot_de_passe_aleatoire}")
            enregistrer_mot_de_passe(mot_de_passe_aleatoire)
        elif choix == "3":
            afficher_mots_de_passe()
        elif choix == "4":
            print("Programme terminé.")
            break
        else:
            print("Choix invalide. Veuillez choisir 1, 2, 3, ou 4.")

if __name__ == "__main__":
    programme()