from db_init import * 
import random

def show_main_menu():
    print("=================== Bienvenue dans le jeu de combat ! ===================")
    print("1. Lancer le jeu")
    print("2. Afficher le tableau des scores")
    print("3. Quitter")
    print("==========================================================\n")

def is_valid(saisie, max_val, min_val):
    if not saisie.isnumeric():
        return False
    if int(saisie) > max_val:
        return False
    if int(saisie) < min_val:
        return False
    return True 


def verifier_nombre_valide(min_val, max_val, message):
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

def choose_characters():
    equipe = []
    print("\n=================== Choisissez votre équipe ! ===================")
    print("Voici les personnages diponibles :")
    # Recuperer liste des personnages de la base
    personnages = get_available_characters()
    print("==========================================================\n")
    # Faire une boucle pour que ça se répete le temps que l'équipe n'est pas complète (3 personnages)
    while not is_equipe_full(equipe):
        # Afficher les personnages disponibles
        show_available_characters(personnages)
        # Demander de choisir un personnages
        choix = input("Veuillez choisir un personnages à ajouté dans votre équipe : ")
        # Si le personnages est Valide
        if is_characteres_valid(choix, personnages):
            choix = int(choix)
            # l'envoyer dans l'équipe
            equipe.append(personnages[choix])
            # le supprimé de la liste des personnagess disponibles
            personnages.pop(choix)
    return equipe


def get_random_monster(liste_monstres):
    # Choisir un monstre au hasard
    monstre = random.choice(liste_monstres)
    return monstre


def is_alive(personnage):
    #  Verifier si le personnage est toujours en vie 
    if personnage["HP"] > 0:
        return True
    else:
        return False

def ennemi_is_dead(ennemi):
    # Verifier si l'ennemi est mort 
    if ennemi["HP"] <= 0:
        return True
    else:
        return False

def equipe_is_dead(equipe):
    # Verifier si l'equipe est morte
    for membre in equipe:
        # Si un membre est vivant return False
        if is_alive(membre):
            return False
        # Sinon return True
    return True

def count_damage(attaquant, defenseur):
    # Calculer les dégats de l'attaque en fonction de la défense de l'ennemi
    degats = attaquant["ATK"] - defenseur["DEF"]
    # Si les dégats sont inferieur à 1 on met les dégat aléatoire 
    if degats < 1:
        degats = 2 * random.randint(1, 10 )
    return degats

def show_etat_fight(equipe, ennemi):
    # Afficher la vie de l'équipe 
    print("\n=================== État du combat ===================")
    for membre in equipe:
        print(f"  {membre['NAME']} | HP: {membre['HP']}")
    # Afficher la vie de l'ennemi
    print(f"\n  {ennemi['NAME']} | HP: {ennemi['HP']}")

def equipe_hit_ennemi(equipe, ennemi):
    # Faire attaquer chaque membre de l'équipe si il est en vie à l'ennemi
    for membre in equipe:
        # Si il est en vie lui faire des dégats
        if is_alive(membre):
            degats = count_damage(membre, ennemi)
            ennemi["HP"] -= degats
            print(f"{membre['NAME']} attaque {ennemi['NAME']} et inflige {degats} points de dégats !")

def ennemi_hit_equipe(equipe, ennemi):
    # Récupérer uniquement les membres vivants
    membres_vivants = [m for m in equipe if is_alive(m)]
    # Choisir un membre vivant de l'équipe au hasard pour l'attaquer
    membre = random.choice(membres_vivants)
    degats = count_damage(ennemi, membre)
    membre["HP"] -= degats
    print(f"{ennemi['NAME']} attaque {membre['NAME']} et inflige {degats} points de dégat !")
    if not is_alive(membre):
        print(f"{membre['NAME']} est mort !")

def start_fight(equipe, ennemi):
    print(f"\n=================== Combat contre {ennemi['NAME']} ! ===================")
    # Boucle du combat jusqu'a la mort de l'ennemi ou de l'équipe
    while not ennemi_is_dead(ennemi) and not equipe_is_dead(equipe):
        # Afficher la vie de l'équipe et du boss
        show_etat_fight(equipe, ennemi)
        # Vérifier si le personnage est encore en vie pour attaquer
        equipe_hit_ennemi(equipe, ennemi)
        # Vérifier si l'ennemi est mort après les attaque
        if not ennemi_is_dead(ennemi):
            # L'ennemi attaque un membre aléatoire
            ennemi_hit_equipe(equipe, ennemi)
    show_etat_fight(equipe, ennemi)


def get_noms_personnages(equipe):
    # affiche le nom des personnages pour les afficher au moment de voir le score
    # faire un liste pour les stocker
    noms_personnages = []
    for membre in equipe:
        noms_personnages.append(membre["NAME"])
    return noms_personnages


def enregistrer_score(team_name, vague, equipe):
    # Recuperer les noms des personnages
    noms_personnages = get_noms_personnages(equipe)
    # Enregistrer le score
    add_attemps(team_name, vague, noms_personnages)


def show_equipe(team_name, equipe):
    print(f"\n=================== Équipe {team_name} ===================")
    for membre in equipe:
        print(f"  {membre['NAME']} | ATK: {membre['ATK']} | DEF: {membre['DEF']} | HP: {membre['HP']}")
    print("==========================================================\n")


def start_battles(equipe, team_name):
    vague = 1
    liste_monstres = get_available_monster()
    # Boucle tant que pour que le combat continue tant qu'une des deux conditions n'est pas remplie
    while True:
        print(f"\n=================== Vague {vague} ===================")
        
        # choisir un ennemi aléatoirement
        ennemi = get_random_monster(liste_monstres)

        # Faire un systeme Tour par tour 
        start_fight(equipe, ennemi)

        # En cas de victoire quand l'ennemi est mort
        if equipe_is_dead(equipe):
            # Si l'équipe meurt finir la partie
            print("\n=================== Vous avez perdu ! ===================")
            print(f"Votre équipe est morte à la vague {vague} !")
            break
            
        else:
            # lancer une autre vague
            print(f"Vague {vague} terminée !")
            vague = vague + 1

    #enregistrer le score
    enregistrer_score(team_name, vague, equipe)


def start_game(): 
    # Demander de crée son équipe (contient un nom valides et 3 personnages valides)
    team_name = ask_team_name()

    # Demander à l'utilisateur de choisir 3 personnages pour son équipe
    equipe = choose_characters()

    show_equipe(team_name, equipe)

    # Lancer les combats
    start_battles(equipe, team_name)
   
def show_board():
    # Récuperer tout les scores 
    # Si il n'y a pas de score, afficher un message
    # Sinon on affiche les différents scores un par un
    ...

def main():
    while True:
        # Afficher le menu principal
        show_main_menu()

        # Demander à l'utilisateur de choisir une option
        choix_utilisateur = verifier_nombre_valide(1, 3, "Veuillez choisir une option (1-3) : ")

        if choix_utilisateur == "1":
            # lancer le jeu
            start_game()

        if choix_utilisateur == "2":
            # Afficher le tableau des scores
            show_board()

        if choix_utilisateur == "3":
            # Quitter le programme
            print("Merci d'avoir joué ! À bientôt !")
            exit()


main()


