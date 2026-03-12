from db_init import * 
from game import *
from utils import *

def show_main_menu():
    print("\n=================== Bienvenue dans le jeu de combat ! ===================\n")
    print("1. Lancer le jeu")
    print("2. Afficher le tableau des scores")
    print("3. Quitter")
    print("\n==========================================================\n")

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
    scores = get_all_attemps()
    # Si il n'y a pas de score, afficher un message
    if len(scores) == 0:
        print("Vous n'avez pas de scores disponible !")
    # Sinon on affiche les différents scores un par un
    else:
        for score in scores:
            print(f"\n=================== {score['NAME']}  ===================\n")
            print(f"| Vague: {score['VAGUE']} | membre: {score['CHARACTERS']}")
            print("\n==========================================================\n")

def main():
    while True:
        # Afficher le menu principal
        show_main_menu()

        # Demander à l'utilisateur de choisir une option
        choix_utilisateur = recuperer_nombre_valide(1, 3, "Veuillez choisir une option (1-3) : ")

        if choix_utilisateur == "1":
            # lancer le jeu
            start_game()

        if choix_utilisateur == "2":
            # Afficher le tableau des scores
            show_board()

        if choix_utilisateur == "3":
            # Quitter le programme
            print("=========================================================================")
            print(f"                   Merci d'avoir joué ! À bientôt !                     ")
            print("=========================================================================\n")
            exit()


main()


