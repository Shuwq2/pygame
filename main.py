from db_init import * 
import random

def show_main_menu():
    print("=================== Bienvenue dans le jeu de combat ! ===================")
    print("1. Lancer le jeu")
    print("2. Afficher le tableau des scores")
    print("3. Quitter")

def is_valid(saisie,max_val,min_val):
    if not saisie.isnumeric():
        return False
    if int(saisie) > max_val:
        return False
    if int(saisie) < min_val:
        return False
    return True 


def verifier_nombre_valide(min_val,max_val,message):
    boucle = True
    # Faire une boucle jusqu'à ce que l'utilisateur entre un nombre valide
    while boucle == True:
        # Afficher le message de demande
        print(message)
        # Récupérer l'entrée de l'utilisateur
        saisie = input()
        # Tester si la valeur est dans la plage spécifiée 
        if is_valid(saisie,max_val,min_val):
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

def show_list_choosable_characters(personnages):
    i = 0
    # faire afficher un par un chaque élément de la liste 
    for p in personnages:
        # Afficher les charactères
        print(f"{i}.{p['NAME']} | Attaque: {p['ATK']} | Défense: {p['DEF']} | Vie: {p['HP']}")
        i = i+1

def choose_characters():
    equipe = []
    print("=================== Choisissez votre équipe ! ===================")
    print("Voici les personnages diponibles :")
    # Recuperer liste des personnages de la base
    personnages = get_available_characters()
    # Faire une boucle pour que ça se répete le temps que l'équipe n'est pas complète (3 personnages)
    while not is_equipe_full(equipe):
        # Afficher les personnages disponibles
        show_list_choosable_characters(personnages)
        # Demander de choisir un personnages
        choix = input("Veuillez choisir un personnages à ajouté dans votre équipe : ")
        # Si le personnages est Valide
        if is_characteres_valid(choix,personnages):
            choix = int(choix)
            # l'envoyer dans l'équipe
            equipe.append(personnages[choix])
            # le supprimé de la liste des personnagess disponibles
            personnages.pop(choix)
    return equipe

def get_random_monster():
    monsters = get_available_monster()
    monsters_random = random.choices(monsters, k=1)
    return monsters_random

def start_fight():
    ...

def start_battles():
    vague = 1
    # qui va selectionner l'équipe
    equipe = choose_characters()
    # choisir un ennemi aléatoirement
    ennemi = get_random_monster()

    # Faire un systeme Tour par tour 
    start_fight()

    # En cas de victoire (quand l'ennemi est mort)
    if ennemi_isdead():
    # lancer une autre vague
        vague += 1
        # supprimé l'ancien ennemi de la liste des ennemie
        get_random_monster()
    else:
        # Si l'équipe meurt finir la partie
        if equipe_isdead() == True:
            #enregistrer le score
            get_score()
            #renvoyer au menu principal        
 


def start_game(): 
    # Demander de crée son équipe (contient un nom valides et 3 personnages valides)
    ask_team_name()

    # Demander à l'utilisateur de choisir 3 personnages pour son équipe
    choose_characters()

    # Lancer les combats
    start_battles()
   

def main():
    # Afficher le menu principal
    show_main_menu()

    # Demander à l'utilisateur de choisir une option
    choix_utilisateur = verifier_nombre_valide(1, 3, "Veuillez choisir une option (1-3) : ")

    # En fonction du choix de l'utilisateur, appeler la fonction correspondante
    if choix_utilisateur == "1":
        # lancer le jeu
        start_game()
        

    if choix_utilisateur == "2":
        # Afficher le tableau des scores
        show_board()

    if choix_utilisateur == "3":
        # Quitter le programme
        exit()


