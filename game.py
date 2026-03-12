from utils import *
import random

def choose_characters():
    equipe = []
    print("\n=================== Choisissez votre équipe ! ===================\n")
    print("Voici les personnages diponibles :")
    # Recuperer liste des personnages de la base
    personnages = get_available_characters()
    
    # Faire une boucle pour que ça se répete le temps que l'équipe n'est pas complète (3 personnages)
    while not is_equipe_full(equipe):
        # Afficher les personnages disponibles
        show_available_characters(personnages)
        print("\n==========================================================\n")
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
    print("\n=================== État du combat ===================\n")
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
    print(f"\n=================== Combat contre {ennemi['NAME']} ! ===================\n")
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
    # Afficher chaque membre de l'équipe
    print(f"\n=================== Équipe {team_name} ===================")
    for membre in equipe:
        print(f"  {membre['NAME']} | ATK: {membre['ATK']} | DEF: {membre['DEF']} | HP: {membre['HP']}")
    print("==========================================================\n")


def start_battles(equipe, team_name):
    vague = 1
    liste_monstres = get_available_monster()
    # Boucle tant que pour que le combat continue tant qu'une des deux conditions n'est pas remplie
    while True:
        print(f"\n=================== Vague {vague} ===================\n")
        
        # choisir un ennemi aléatoirement
        ennemi = get_random_monster(liste_monstres)

        # Faire un systeme Tour par tour 
        start_fight(equipe, ennemi)

        # En cas de victoire quand l'ennemi est mort
        if equipe_is_dead(equipe):
            # Si l'équipe meurt finir la partie
            print("\n=================== Vous avez perdu ! ===================")
            print(f"Votre équipe est morte à la vague {vague} !")
            print("=========================================================\n")
            break
            
        else:
            # lancer une autre vague
            print(f"Vague {vague} terminée !")
            vague = vague + 1

    #enregistrer le score
    enregistrer_score(team_name, vague, equipe)
