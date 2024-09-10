#Variables globales qui vont être modifiées dans les fonctions
nom_compte = ''
solde_compte = 0
mdp_compte = ''

def nouveau_compte(nom, solde, mdp):
    """
    Crée un nouveau compte bancaire avec un nom, un solde initial et un mot de passe.

    Paramètres :
    nom (str) : Le nom du titulaire du compte.
    solde (float) : Le solde initial du compte.
    mdp (str) : Le mot de passe du compte.
    """
    pass

def afficher():
    """
    Affiche les détails du compte, incluant le nom du titulaire, le solde et le mot de passe.
    """
    pass

def obtenir_solde(mdp):
    """
    Retourne le solde du compte si le mot de passe fourni est correct.

    Paramètres :
    mdp (str) : Le mot de passe pour accéder au solde du compte.

    Retourne :
    float : Le solde du compte ou None si le mot de passe est incorrect.
    """
    pass

def deposer(montant, mdp):
    """
    Dépose un montant dans le compte si le mot de passe est correct et le montant positif.

    Paramètres :
    montant (float) : Le montant à déposer.
    mdp (str) : Le mot de passe du compte.

    Retourne :
    float : Le nouveau solde du compte ou None si le montant est négatif ou le mot de passe incorrect.
    """
    pass

def retirer(montant, mdp):
    """
    Retire un montant du compte si le montant est positif, le mot de passe correct, et le solde suffisant.

    Paramètres :
    montant (float) : Le montant à retirer.
    mdp (str) : Le mot de passe du compte.

    Retourne :
    float : Le nouveau solde du compte ou None si le montant est négatif, le mot de passe incorrect,
            ou le solde insuffisant.
    """
    pass

# This is where the functions are tested
while True:
    print()
    print('Appuyez sur n pour nouveau compte')
    print('Appuyez sur s pour voir le solde')
    print('Appuyez sur d pour faire un dépôt')
    print('Appuyez sur r pour faire un retrait')
    print('Appuyez sur a pour afficher le compte')
    print('Appuyez sur q pour quitter')
    print()

    action = input('Que souhaitez-vous faire ? ')
    action = action.lower()  # force en minuscules
    action = action[0]  # utilise juste la première lettre
    print()

    # This is where an account is created
    if action == 'n':
        print('Nouveau compte :')
        nouveau_compte(nom_compte, solde_compte, mdp_compte)

    # Get the bank balance
    elif action == 's':
        print('Obtenir le Solde :')
        obtenir_solde(mdp_compte)

    # Deposits an amount
    elif action == 'd':
        print('Dépôt :')
        deposer(solde_compte, mdp_compte)


    # Withdraws an amount
    elif action == 'r':
        print('Retrait :')
        retirer(solde_compte, mdp_compte)

    # Shows the bank acc information
    elif action == 'a':
        print('Affichage des informations du compte :')
        afficher()

    # Exits the while loop
    elif action == 'q':
        print('Vous avez choisi de quitter. À bientôt !')
        break

    print('Opération terminée.')
    
