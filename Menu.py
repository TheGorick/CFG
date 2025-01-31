#Caroline Ceus-Dorphelus
#Félix-Antonin Noël
#Guillaume Pinat

import Bibliotheque as Bibliotheque
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit
from functools import partial

class Menu(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 300, 400)
        self.bibliotheque = Bibliotheque.Bibliotheque()

        layout = QVBoxLayout()  # QVBoxLayout permet d'empiler les boutons verticalement.

        self.boutons = [
            QPushButton("1 - Ajouter un abonné"),
            QPushButton("2 - Supprimer un abonné"),
            QPushButton("3 - Afficher tous les abonnés"),
            QPushButton("4 - Ajouter un document"),
            QPushButton("5 - Supprimer un document"),
            QPushButton("6 - Afficher tous les documents"),
            QPushButton("7 - Emprunt"),
            QPushButton("8 - Retour"),
            QPushButton("9 - Afficher tous les emprunts"),
            QPushButton("Q - Quitter")
        ]

        for i, bouton in enumerate(self.boutons):  # Parcourt la liste des boutons tout en récupérant l'index (i) et l'objet bouton (bouton)
            layout.addWidget(bouton)  # Ajout du bouton au layout
            bouton.clicked.connect(partial(self.active_choix, i + 1))  # CHAT GPT WAS HERE! Explication juste après
            """ 
            Dans PyQt, la méthode clicked.connect() ne permet pas de passer directement des arguments à une fonction.
            On utilise donc lambda ou functools.partial pour ajouter un paramètre à active_choix().

            Problème sans lambda ou partial :
            bouton.clicked.connect(self.active_choix(i + 1)) # Cette ligne exécuterait immédiatement self.active_choix(i + 1) au moment de la boucle, au lieu d'attendre un clic et ce sera donc toujours le dernier index

            functools.partial est une fonction du module standard functools qui permet de préremplir certains arguments d'une fonction. Il retourne une nouvelle fonction avec ces arguments déjà fixés.
            C'est une alternative plus propre à lambda quand on doit passer des arguments à une fonction connectée à un signal PyQt.
            """

        # Ajout d'un champ de saisie pour la sélection par clavier
        self.saisie = QLineEdit()  # Permet d'entrer un chiffre ou "Q/q" pour exécuter une action.
        self.saisie.setPlaceholderText("Entrez un chiffre (1-9) ou Q/q pour quitter")
        self.saisie.returnPressed.connect(self.cleanup)
        layout.addWidget(self.saisie)

        self.setLayout(layout)

    def cleanup(self):
        text = self.saisie.text().strip()  # Récupère le texte et enlève les espaces
        self.saisie.clear()  # Efface le champ de saisie
        if text.isdigit():  # Si c'est un chiffre
            choix = int(text)  # Convertit le texte en entier
            if 1 <= choix <= 9:  # Si l'option est entre 1 et 9
                self.active_choix(choix)  # Appelle la fonction active_choix avec l'option choisie
            else:
                print("Option invalide, veuillez entrer un chiffre entre 1 et 9.")  # Message d'erreur pour option invalide
        elif text.lower() == 'q':
            self.close()  # Ferme la fenêtre
        else:
            print("Entrée invalide. Veuillez entrer un chiffre entre 1 et 9 ou 'Q' pour quitter.")  # Message pour entrée invalide

    def active_choix(self, choix):
        fonctions = {
            1: self.activer_ajout_abonne,
            2: self.activer_supprimer_abonne,
            3: self.bibliotheque.afficher_abonnes,
            4: self.activer_ajout_document,
            5: self.activer_supprimer_document,
            6: self.bibliotheque.afficher_documents,
            7: self.activer_emprunt_retour,
            8: self.activer_emprunt_retour,
            9: self.bibliotheque.afficher_emprunts,
            10: self.close
        }
        fonctions[choix]()  # Appelle la fonction

    def activer_ajout_abonne(self):
        prenom = input("Entrez le prénom de l'abonné : ")
        nom = input("Entrez le nom de l'abonné : ")
        mail = input("Entrez le mail de l'abonné : ")
        if self.bibliotheque.ajouter_abonne(prenom, nom, mail):
            print("Abonné ajouté avec succès.")
        else:
            print("L'abonné existe déjà.")

    def activer_supprimer_abonne(self):
        prenom = input("Entrez le prénom de l'abonné : ")
        nom = input("Entrez le nom de l'abonné : ")
        mail = input("Entrez le mail de l'abonné : ")
        if self.bibliotheque.supprimer_abonne(prenom, nom, mail):
            print("Abonné supprimer avec succès.")
        else:
            print("L'abonné n'existe pas.")

    def activer_ajout_document(self):
        classification = input("Entrez le type de document : ")
        titre = input("Entrez le titre du document : ")
        if self.bibliotheque.ajouter_document(classification, titre):
            print("Document ajouté avec succès.")
        else:
            print("Le document est déjà dans la bibliothèque.")

    def activer_supprimer_document(self):
        titre = input("Entrez le titre du document : ")
        if self.bibliotheque.supprimer_document(titre):
            print("Document supprimé avec succès.")
        else:
            print("Document n'existe pas.")

    def activer_emprunt_retour(self):
        identifiant = input("Entrez le titre ou l'ID du document : ")
        if not self.bibliotheque.retour(identifiant):
            print(f"Document '{identifiant}' non trouvé.")