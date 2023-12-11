import hashlib  # Librairie pour le hashage de mot de passe.

mot_de_passe = input("Entrez votre mot de passe : ")  # On demande à l'utilisateur d'entrer son mot de passe.

if len(mot_de_passe) < 8:  # Si le mot de passe est inférieur à 8 caractères ca mettra une phrase d'erreurs.
    print("Mot de passe trop court !")  # On affiche un message d'erreur.
elif mot_de_passe.isupper(): # Si le mot de passe contient que des majuscules ca mettra une phrase d'erreurs.
    print("Le mot de passe contient que des majuscule !")  # On affiche un message d'erreur.
elif mot_de_passe.islower(): # Si le mot de passe contient que des minuscules ca mettra une phrase d'erreurs.
    print("Le mot de passe contient que des minuscule !")  # On affiche un message d'erreur.
