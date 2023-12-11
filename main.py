import hashlib  # Librairie pour le hashage de mot de passe.

def caracteres_speciaux(mot_de_passe): # Si le mot de passe contient des caractères spéciaux ca mettra une phrase d'erreurs.
    global caracteres_special
    for i in caracteres_special:
        if i in mot_de_passe:
            return True
    return False

caracteres_special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"] # On crée une liste de caractères spéciaux.

mot_de_passe = input("Entrez votre mot de passe : ")  # On demande à l'utilisateur d'entrer son mot de passe.
if len(mot_de_passe) < 8:  # Si le mot de passe est inférieur à 8 caractères ca mettra une phrase d'erreurs.
    print("Le mot de passe est trop court il doit au moins contenir 8 caractères.")  # On affiche un message d'erreur.
elif mot_de_passe.isalpha(): # Si le mot de passe contient que des lettres ca mettra une phrase d'erreurs.
    print("Le mot de passe contient que des lettres")
elif mot_de_passe.isupper(): # Si le mot de passe contient que des majuscules ca mettra une phrase d'erreurs.
    print("Le mot de passe contient que des majuscule")  # On affiche un message d'erreur.
elif mot_de_passe.islower(): # Si le mot de passe contient que des minuscules ca mettra une phrase d'erreurs.
    print("Le mot de passe contient que des minuscule")  # On affiche un message d'erreur.
elif mot_de_passe.isdigit(): # Si le mot de passe contient que des chiffres ca mettra une phrase d'erreurs.
    print("Le mot de passe contient que des chiffres")  # On affiche un message d'erreur.
elif caracteres_speciaux(mot_de_passe) == False: # Si le mot de passe contient des caractères spéciaux ca mettra une phrase d'erreurs.
    print("Votre mot de passe doit contenir au moins un caractère spécial")  # On affiche un message d'erreur.