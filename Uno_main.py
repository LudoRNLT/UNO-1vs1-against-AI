import random
import time

symbole = ('0','1','2','3','4','5','6','7','8','9','PasseTour','ChangementDeSens','+2','+4','ChangementCouleur','Redistribution')
couleur = ('BLEU','ROUGE','VERT','JAUNE')
typeCarte = {'0':'chiffre','1':'chiffre','2':'chiffre','3':'chiffre','4':'chiffre','5':'chiffre','6':'chiffre','7':'chiffre','8':'chiffre','9':'chiffre','PasseTour':'action','ChangementDeSens':'action','+2':'action','+4':'super_action','ChangementCouleur':'super_action','Redistribution':'super_action'}

class Cartes:

    def __init__(self, couleur, symbole):
        self.symbole = symbole
        if typeCarte[symbole] == 'chiffre':
            self.couleur = couleur
            self.typeCarte = 'chiffre'
        elif typeCarte[symbole] == 'action':
            self.couleur = couleur
            self.typeCarte = 'action'
        else :
            self.couleur = None
            self.typeCarte = 'super_action'

    def __str__(self):
        if self.couleur is None:
            return self.symbole
        else:
            return self.couleur + " " + self.symbole

class Pioche:

    def  __init__(self):
        self.pioche = []
        for i in couleur :
            for j in symbole :
                if typeCarte[j] != 'super_action':
                    self.pioche.append(Cartes(i,j))
                    self.pioche.append(Cartes(i,j))
                else :
                    self.pioche.append(Cartes(i,j))
    def __str__(self):
        pioche_restant = ''
        for carte in self.pioche:
            pioche_restant += '\n' + carte.__str__()
        return 'Il y a dans la pioche ' + pioche_restant

    def melanger(self):
        random.shuffle(self.pioche)

    def distribuer(self):
        return self.pioche.pop()
    


    

class JeuEnMain:

    def __init__(self):
        self.cartes = []
        self.strCartes = []
        self.cartesChiffre = 0
        self.cartesAction = 0

    def AjouterCarte(self, carte):
        self.cartes.append(carte)
        self.strCartes.append(str(carte))
        if carte.typeCarte == 'chiffre':
            self.cartesChiffre += 1
        else:
            self.cartesAction += 1

    def EnleverCarte(self,emplacement):
        self.strCartes.pop(emplacement - 1)
        return self.cartes.pop(emplacement -1)

    def CartesEnMain(self):
        for i in range(len(self.strCartes)):
            time.sleep(0.25)
            print(f' {i + 1}.{self.strCartes[i]}')

    def NombreDeCartes(self):
        return len(self.cartes)

    def CarteSeule(self, emplacement):
        return self.cartes[emplacement - 1]

    
#Fonction utiles au gameplay
    
#On choisit qui commence aléatoirement
def Premier():
    if random.randint(0,1) == 0:
        return 'Ordi1'
    else :
        return 'Joueur'

#Verifie si un joueur a gagné
def victoire(jeu):
    if len(jeu.cartes) == 0:
        return True
    return False

#Vérifie si le joueur qui termine finit bien par une carte chiffre
def DerniereCartePosee(jeu):
    for k in jeu.cartes:
        if k.typeCarte != 'chiffre':
            return True
        else:
            return False

#Regarde si la carte à poser est valide en la comparant avec le haut de la pile
def CartePoseeValide(CarteEnHautDePile,carte):
    if carte.symbole == CarteEnHautDePile.symbole or CarteEnHautDePile.couleur == carte.couleur or carte.typeCarte == 'super_action':
        return True
    else :
        return False

#Regarde si l'ordi adverse a une carte à jouer
def OrdiAction(jeu,CarteEnHautDePile):
    for k in jeu.cartes:
        if k.symbole == CarteEnHautDePile.symbole or k.couleur == CarteEnHautDePile.couleur or k.typeCarte == 'super_action':
            return jeu.EnleverCarte(jeu.strCartes.index(str(k))+1)
    else :
        return "pas de cartes à jouer"

#Début de la boucle de gameplay

while True:

    print("\nJEU DU UNO !")

    pioche = Pioche()
    pioche.melanger()

    jeu_joueur = JeuEnMain()
    for i in range(7):
        jeu_joueur.AjouterCarte(pioche.distribuer())

    jeu_Ordi1 = JeuEnMain()
    for i in range(7):
        jeu_Ordi1.AjouterCarte(pioche.distribuer())

    CarteEnHautDePile = pioche.distribuer()
    if CarteEnHautDePile.typeCarte != "chiffre" :
        while CarteEnHautDePile.typeCarte != "chiffre":
            CarteEnHautDePile = pioche.distribuer()
            
    print("\nLa carte de départ est: {}".format(CarteEnHautDePile))
    time.sleep(1)
    
    gameplay = True

    tour = Premier()
    print('\n'+ tour + " jouera en premier")

    while gameplay:

        if tour == "Ordi1":
            if jeu_Ordi1.NombreDeCartes() == 1:
                if DerniereCartePosee(jeu_Ordi1):
                    time.sleep(1)
                    print("L'ordinateur pioche une carte")
                    jeu_Ordi1.AjouterCarte(pioche.distribuer())
            CartePossible = OrdiAction(jeu_Ordi1, CarteEnHautDePile)
            time.sleep(1)
            if CartePossible != "pas de cartes à jouer":
                print(f"\nL'ordinateur a joué : {CartePossible}")
                time.sleep(1)
                if CartePossible.typeCarte == "chiffre":
                    CarteEnHautDePile = CartePossible
                    tour = 'Joueur'
                else  :
                    if CartePossible.symbole == "PasseTour":
                        tour = "Ordi1"
                        CarteEnHautDePile = CartePossible
                    elif CartePossible.symbole == "ChangementDeSens":
                        turn = "Ordi1"
                        CarteEnHautDePile = CartePossible
                    elif CartePossible.symbole == "+2":
                        for i in range (2):
                            jeu_joueur.AjouterCarte(pioche.distribuer())
                        CarteEnHautDePile = CartePossible
                        tour = 'Ordi1'
                    elif CartePossible.symbole =='+4':
                        for i in range(4):
                            jeu_joueur.AjouterCarte(pioche.distribuer())
                        CarteEnHautDePile = CartePossible
                        a = random.randint(1, 4)
                        if a == 1:
                            CouleurPlus4 = "ROUGE"
                        elif a == 2:
                            CouleurPlus4 = "BLEU"
                        elif a == 3:
                            CouleurPlus4 = "JAUNE"
                        else :
                            CouleurPlus4 = "VERT"
                        CarteEnHautDePile.couleur = CouleurPlus4
                        print("L'ordinateur a choisi la couleur : ", CouleurPlus4)
                        tour = 'Ordi1'
                    elif CartePossible.symbole == 'ChangementCouleur':
                        CarteEnHautDePile = CartePossible
                        a = random.randint(1, 4)
                        if a == 1:
                            ChangementCouleurC = "ROUGE"
                        elif a == 2:
                            ChangementCouleurC = "BLEU"
                        elif a == 3:
                            ChangementCouleurC = "JAUNE"
                        else :
                            ChangementCouleurC = "VERT"
                        CarteEnHautDePile.couleur = ChangementCouleurC
                        print("L'ordinateur a choisi la couleur : ", ChangementCouleurC)
                        tour = 'Joueur'
                    elif CartePossible.symbole == 'Redistribution':
                        CarteEnHautDePile = CartePossible
                        redi = jeu_Ordi1.NombreDeCartes() + jeu_joueur.NombreDeCartes()
                        for i in range(jeu_Ordi1.NombreDeCartes()):
                            jeu_Ordi1.EnleverCarte(0)
                        for i in range(jeu_joueur.NombreDeCartes()):
                            jeu_joueur.EnleverCarte(0)
                        if redi%2 == 0:
                            for i in range(int(redi/2)):
                                jeu_Ordi1.AjouterCarte(pioche.distribuer())
                                jeu_joueur.AjouterCarte(pioche.distribuer())
                        else:
                            for i in range(int((redi-1)/2)):
                                jeu_Ordi1.AjouterCarte(pioche.distribuer())
                            for i in range(int((redi+1)/2)):
                                jeu_joueur.AjouterCarte(pioche.distribuer())
                        a = random.randint(1, 4)
                        if a == 1:
                            CouleurRedi = "ROUGE"
                        elif a == 2:
                            CouleurRedi = "BLEU"
                        elif a == 3:
                            CouleurRedi = "JAUNE"
                        else :
                            CouleurRedi = "VERT"
                        CarteEnHautDePile.couleur = CouleurRedi
                        print("\nLes jeux ont été redistribué équitablement")
                        time.sleep(0.5)
                        print("\nL'ordinateur a choisi la couleur :", CouleurRedi)
                        tour = 'Joueur'

            else :
                print("\nL'ordinateur pioche une carte")
                time.sleep(1)
                CartePossible = pioche.distribuer()
                if CartePoseeValide(CarteEnHautDePile, CartePossible):
                    print(f"\nL'ordinateur a joué : {CartePossible}")
                    time.sleep(1)
                    if CartePossible.typeCarte == "chiffre":
                        CarteEnHautDePile = CartePossible
                        tour = 'Joueur'
                    else  :
                        if CartePossible.symbole == "PasseTour":
                            tour = "Ordi1"
                            CarteEnHautDePile = CartePossible
                        elif CartePossible.symbole == "ChangementDeSens":
                            turn = "Ordi1"
                            CarteEnHautDePile = CartePossible
                        elif CartePossible.symbole == "+2":
                            for i in range (2):
                                jeu_joueur.AjouterCarte(pioche.distribuer())
                            CarteEnHautDePile = CartePossible
                            tour = 'Ordi1'
                        elif CartePossible.symbole =='+4':
                            for i in range(4):
                                jeu_joueur.AjouterCarte(pioche.distribuer())
                            CarteEnHautDePile = jeu_joueur.EnleverCarte(choix)
                            a = random.randint(1, 4)
                            if a == 1:
                                CouleurPlus4 = "ROUGE"
                            elif a == 2:
                                CouleurPlus4 = "BLEU"
                            elif a == 3:
                                CouleurPlus4 = "JAUNE"
                            else :
                                CouleurPlus4 = "VERT"
                            CarteEnHautDePile.couleur = CouleurPlus4
                            print("L'ordinateur a choisi la couleur :", Couleur+4)
                            tour = 'Ordi1'
                        elif CartePossible.symbole == 'ChangementCouleur':
                            CarteEnHautDePile = CartePossible
                            a = random.randint(1, 4)
                            if a == 1:
                                ChangementCouleurC = "ROUGE"
                            elif a == 2:
                                ChangementCouleurC = "BLEU"
                            elif a == 3:
                                ChangementCouleurC = "JAUNE"
                            else :
                                ChangementCouleurC = "VERT"
                            CarteEnHautDePile.couleur = ChangementCouleurC
                            print("L'ordinateur a choisi la couleur : ", ChangementCouleurC)
                            tour = 'Joueur'
                        elif CartePossible.symbole == 'Redistribution':
                            CarteEnHautDePile = CartePossible
                            redi = jeu_Ordi1.NombreDeCartes() + jeu_joueur.NombreDeCartes()
                            for i in range(jeu_Ordi1.NombreDeCartes()):
                                jeu_Ordi1.EnleverCarte(0)
                            for i in range(jeu_joueur.NombreDeCartes()):
                                jeu_joueur.EnleverCarte(0)
                            if redi%2 == 0:
                                for i in range(int(redi/2)):
                                    jeu_Ordi1.AjouterCarte(pioche.distribuer())
                                    jeu_joueur.AjouterCarte(pioche.distribuer())
                            else:
                                for i in range(int((redi-1)/2)):
                                    jeu_Ordi1.AjouterCarte(pioche.distribuer())
                                for i in range(int((redi+1)/2)):
                                    jeu_joueur.AjouterCarte(pioche.distribuer())
                            a = random.randint(1, 4)
                            if a == 1:
                                CouleurRedi = "ROUGE"
                            elif a == 2:
                                CouleurRedi = "BLEU"
                            elif a == 3:
                                CouleurRedi = "JAUNE"
                            else :
                                CouleurRedi = "VERT"
                            CarteEnHautDePile.couleur = CouleurRedi
                            print("\nLes jeux ont été redistribué équitablement")
                            time.sleep(0.5)
                            print("\nL'ordinateur a choisi la couleur :", CouleurRedi)
                            tour = 'Joueur'
                            
                else :
                    print("L'ordinateur n'a aucune cartes valides à jouer")
                    time.sleep(1)
                    jeu_Ordi1.AjouterCarte(pioche.distribuer())
                    tour = 'Joueur'
            print("\nIl reste à l'ordinateur {} cartes".format(jeu_Ordi1.NombreDeCartes()))
            time.sleep(1)
            if victoire(jeu_Ordi1):
                print("\nL'ordinateur a gagné !!")
                gameplay = False
                break
                
        if tour =='Joueur' :
            time.sleep(1)
            print('\nLa carte en haut de la pile est :' + str(CarteEnHautDePile))
            time.sleep(1)
            print('\nVotre jeu :\n')
            jeu_joueur.CartesEnMain()
            if jeu_joueur.NombreDeCartes() == 1:
                print("\n UNO !")
                if DerniereCartePosee(jeu_joueur):
                    print('La dernière carte doit être un chiffre')
                    print("\n Pioche automatique d'une carte")
                    jeu_joueur.AjouterCarte(pioche.distribuer())
                    print('Votre jeu :')
                    jeu_joueur.CartesEnMain()
            time.sleep(1)
            print('\nJouer une carte ou piocher ?')
            time.sleep(0.5)
            action = input('J/j pour Jouer \nP/p pour Piocher : ')
            action = action.upper()
            if action == 'P':
                CartePossible = pioche.distribuer()
                print('Vous avez pioché :' + str(CartePossible))
                time.sleep(1)
                if CartePoseeValide(CarteEnHautDePile, CartePossible):
                    jeu_joueur.AjouterCarte(CartePossible)
                else :
                    print('Vous ne pouvez pas jouer la carte piochée')
                    jeu_joueur.AjouterCarte(CartePossible)
                    tour = 'Ordi1'
            elif action == 'J' :
                choix = int(input("Entrez l'index de la carte que vous voulez jouer : "))
                while choix > jeu_joueur.NombreDeCartes() or choix < 1 :
                    choix = int(input('Veuillez saisir une valeur correcte : '))
                CartePossible = jeu_joueur.CarteSeule(choix)
                if CartePoseeValide(CarteEnHautDePile, CartePossible):
                    if CartePossible.typeCarte == 'chiffre':
                        CarteEnHautDePile = jeu_joueur.EnleverCarte(choix)
                        tour = 'Ordi1'
                    else :
                        if CartePossible.symbole == 'ChangementDeSens' or CartePossible.symbole == 'PasseTour':
                            CarteEnHautDePile = jeu_joueur.EnleverCarte(choix)
                            tour = 'Joueur'
                        elif CartePossible.symbole == '+2':
                            print("\nL'ordinateur pioche 2 cartes")
                            for i in range(2):
                                jeu_Ordi1.AjouterCarte(pioche.distribuer())
                            CarteEnHautDePile = jeu_joueur.EnleverCarte(choix)
                            tour = 'Joueur'
                        elif CartePossible.symbole == '+4':
                            print("\nL'ordinateur pioche 4 cartes")
                            for i in range(4):
                                jeu_Ordi1.AjouterCarte(pioche.distribuer())
                            CarteEnHautDePile = jeu_joueur.EnleverCarte(choix)
                            while True :
                                CouleurPlus4 = input('Saisissez une couleur : ')
                                CouleurPlus4 = CouleurPlus4.upper()
                                if CouleurPlus4 == 'ROUGE' or CouleurPlus4 == 'BLEU' or CouleurPlus4 == 'JAUNE' or CouleurPlus4 == 'VERT':
                                    break
                            CarteEnHautDePile.couleur = CouleurPlus4
                            tour = 'Joueur'
                        elif CartePossible.symbole == 'ChangementCouleur':
                            CarteEnHautDePile = jeu_joueur.EnleverCarte(choix)
                            
                            while True :
                                ChangementCouleurC = input('Saisissez une couleur : ')
                                ChangementCouleurC = ChangementCouleurC.upper()
                                if ChangementCouleurC == 'ROUGE' or ChangementCouleurC == 'BLEU' or ChangementCouleurC == 'JAUNE' or ChangementCouleurC == 'VERT':
                                    break
                            CarteEnHautDePile.couleur = ChangementCouleurC
                            tour = 'Ordi1'
                        elif CartePossible.symbole == 'Redistribution':
                            CarteEnHautDePile = jeu_joueur.EnleverCarte(choix)
                            redi = jeu_Ordi1.NombreDeCartes() + jeu_joueur.NombreDeCartes()
                            for i in range(jeu_Ordi1.NombreDeCartes()):
                                jeu_Ordi1.EnleverCarte(0)
                            for i in range(jeu_joueur.NombreDeCartes()):
                                jeu_joueur.EnleverCarte(0)
                            if redi%2 == 0:
                                for i in range(int(redi/2)):
                                    jeu_Ordi1.AjouterCarte(pioche.distribuer())
                                    jeu_joueur.AjouterCarte(pioche.distribuer())
                            else:
                                for i in range(int((redi-1)/2)):
                                    jeu_joueur.AjouterCarte(pioche.distribuer())
                                for i in range(int((redi+1)/2)):
                                    jeu_Ordi1.AjouterCarte(pioche.distribuer())

                            print("\nLes jeux ont été redistribué équitablement")
                            time.sleep(0.5)
                            print('\nVotre jeu :\n')
                            jeu_joueur.CartesEnMain()
                            
                            while True :
                                CouleurRedi = input('Saisissez une couleur : ')
                                CouleurRedi = CouleurRedi.upper()
                                if CouleurRedi == 'ROUGE' or CouleurRedi == 'BLEU' or CouleurRedi == 'JAUNE' or CouleurRedi == 'VERT':
                                    break
                            CarteEnHautDePile.couleur = CouleurRedi       
                            tour = 'Ordi1'
                else :
                    print('Cette carte ne peut pas être jouée ici')
            if victoire(jeu_joueur):
                print('\n FELICITATION ! \n Vous avez gagné !')
                gameplay = False
                break
            
    NouvellePartie = input('Voulez-vous jouer une nouvelle partie ? (Oui / Non)')
    NouvellePartie = NouvellePartie.upper()
    if NouvellePartie == 'OUI':
        continue
    else :
        print ("\n Merci d'avoir joué, à bientôt !")
        break

                
