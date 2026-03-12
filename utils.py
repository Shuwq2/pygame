from game import *
from db_init import * 

def is_valid(saisie, max_val, min_val):
    if not saisie.isnumeric():
        return False
    if int(saisie) > max_val:
        return False
    if int(saisie) < min_val:
        return False
    return True 


def recuperer_nombre_valide(min_val, max_val, message):
    boucle = True
    # Faire une boucle jusqu'à ce que l'utilisateur entre un nombre valide
    while boucle == True:
        # Afficher le message de demande
        print(message)
        # Récupérer l'entrée de l'utilisateur
        saisie = input()
        # Tester si la valeur est dans la plage spécifiée 
        if is_valid(saisie, max_val, min_val):
            # Si c'est le cas, retourner la valeur
            return saisie        
        else:
            # Sinon, afficher un message d'erreur et recommencer la boucle
            print("Veuillez entrer un nombre valide.")


def team_name_is_valid(team_name):
        # Verifier si le nom est compris entre 3 et 20 charactères
        if len(team_name) <= 3 or len(team_name) >= 20:
            print("Le nom de votre équipe doit contenir entre 3 et 20 charactères")
        else:
            return team_name
        

def ask_team_name():
    # Boucle tant que pour que ça se répète si le nom n'est pas valide
    while True :
        # Demander à l'utilisateur de choisir un nom pour son équipe
        team_name = input("Veuillez choisir un nom pour votre équipe : ")
        # Vérifier si l'input est valide
        if team_name_is_valid(team_name):
            return team_name

def get_available_characters():
    liste_characteres = []
    # Prendre chaque élément de la base de donnée
    for character in characters_collection.find({}, {"NAME": 1, "ATK": 1, "DEF": 1, "HP": 1, "_id": 0}):
        # Ajouter les éléments dans une liste 
        liste_characteres.append(character)

    return liste_characteres

def get_available_monster():
    liste_monsters = []
    # Prendre chaque élément de la base de donnée
    for monster in monsters_collection.find({}, {"NAME": 1, "ATK": 1, "DEF": 1, "HP": 1, "_id": 0}):
        # Ajouter les éléments dans une liste 
        liste_monsters.append(monster)

    return liste_monsters


def is_equipe_full(equipe):
    # Verifier si l'équipe contient 3 membres
    if len(equipe) == 3:
        # Si l'équipe est complète renvoyer True
        return True
    # Si ne contient pas 3 membres envoie un message d'erreur ou False
    else:
        return False
    
def is_characteres_valid(choix, personnage):
    # Vérifier si le choix est un nombre
    if not choix.isdigit():
        print("Veuillez rentrer un numéro valide !")
        return False
    
    choix = int(choix)
    # Vérifier si le choix correspond à un personnage
    if choix < 0 or choix >= len(personnage):
        print("Choix invalide")
        return False
    return True

def show_available_characters(personnages):
    i = 0
    # faire afficher un par un chaque élément de la liste 
    for p in personnages:
        # Afficher les charactères
        print(f"{i}.{p['NAME']} | Attaque: {p['ATK']} | Défense: {p['DEF']} | Vie: {p['HP']}")
        i = i + 1