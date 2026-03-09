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
    # Boucle tant que 
    while True:
        # Verifier si le nom est compris entre 3 et 20 charactères
        # si le nom est inférieur ou égal à 3 
        if len(team_name) <= 3:
            print("Le nom de votre équipe doit contenir au moins 3 charactères")
            return True
        # si le nom est supérieur ou égal à 20
        if len(team_name) >= 20:
            print("Le nom de votre équipe peux contenir seulement 20 charactères")
            return True
        else:
            return False
        

  

def ask_team_name():
    # Demander à l'utilisateur de choisir un nom pour son équipe
    team_name = input("Veuillez choisir un nom pour votre équipe : ")

    # Vérifier que le nom de l'équipe est valide (pas vide, pas de caractères spéciaux, etc.)
    team_name_is_valid(team_name)

def create_team():
    # Demander à l'utilisateur de choisir un nom pour son équipe
    team_name = ask_team_name()
    
    # Mettre un liste des personnages dans l'équipe de l'utilisateur (vide au début)
    team_characters = []
    # Afficher un message de confirmation de la création de l'équipe
    print(f"l'équipe {team_name} à bien été crée")
    
    

def start_game(): 
    # Demander de crée son équipe (contient un nom valides et 3 personnages valides)
    create_team()

    # Afficher son équipe (nom, personnage choisi)
    show_team()

    # Afficher les personnages disponibles
    show_available_characters()

    # Demander à l'utilisateur de choisir 3 personnages pour son équipe
    choose_characters()

    # Vérifier si les personnages choisis sont valides (existent dans la base de données, pas de doublons, etc.)
    choose_characters_is_valid()

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




main()

