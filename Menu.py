# Guillaume Pinat

from Bibliotheque import Bibliotheque
from Documents import Livre, BandeDessinee
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QInputDialog, QMessageBox
from functools import partial

class Menu(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 300, 400)
        self.bibliotheque = Bibliotheque()  # Création d'une instance de la bibliothèque

        layout = QVBoxLayout()  # QVBoxLayout fait un layout vertical

        # Liste des boutons de l'interface
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

        # Ajoute les boutons au layout et connecte chaque bouton à la méthode active_choix
        for i, bouton in enumerate(self.boutons):
            layout.addWidget(bouton)
            bouton.clicked.connect(partial(self.active_choix, i + 1))  # Utilisation de partial pour ajouter l'index comme argument

        # Champ de saisie pour permettre à l'utilisateur d'entrer un chiffre ou "Q/q" pour quitter
        self.saisie = QLineEdit()
        self.saisie.setPlaceholderText("Entrez un chiffre (1-9) ou Q/q pour quitter")
        self.saisie.returnPressed.connect(self.cleanup)  # Connexion de la touche "Enter" au traitement de la saisie
        layout.addWidget(self.saisie)

        self.setLayout(layout)

    def afficher_message(self, message, titre="Message"):
        # Affiche un message via une boîte de dialogue
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(message)
        msg.setWindowTitle(titre)
        msg.exec()

    def cleanup(self):
        # Récupère le texte de la saisie de l'utilisateur et gère l'entrée
        text = self.saisie.text().strip()
        self.saisie.clear()
        if text.isdigit():  # Si l'utilisateur a entré un chiffre
            choix = int(text)
            if 1 <= choix <= 9:  # Vérifie si le choix est valide
                self.active_choix(choix)  # Exécute la fonction associée à l'option choisie
            else:
                print("Option invalide, veuillez entrer un chiffre entre 1 et 9.")
        elif text.lower() == 'q':  # Si l'utilisateur entre 'q' ou 'Q'
            self.close()
        else:
            print("Entrée invalide. Veuillez entrer un chiffre entre 1 et 9 ou 'Q' pour quitter.")

    def active_choix(self, choix):
        # Dictionnaire de correspondance entre le choix et la fonction à appeler
        fonctions = {
            1: self.activer_ajout_abonne,
            2: self.activer_supprimer_abonne,
            3: self.bibliotheque.afficher_abonnes,
            4: self.activer_ajout_document,
            5: self.activer_supprimer_document,
            6: self.bibliotheque.afficher_documents,
            7: self.activer_emprunt,
            8: self.activer_retour,
            9: self.bibliotheque.afficher_emprunts,
            10: self.close
        }
        fonctions[choix]()  # Appelle la fonction correspondante au choix

    def activer_ajout_abonne(self):
        # Demande le prénom de l'abonné via un QInputDialog
        prenom, ok1 = QInputDialog.getText(self, "Ajouter un abonné", "Entrez le prénom de l'abonné :")
        if not ok1:  # Si l'utilisateur annule la saisie
            return

        # Demande le nom de l'abonné
        nom, ok2 = QInputDialog.getText(self, "Ajouter un abonné", "Entrez le nom de l'abonné :")
        if not ok2:
            return

        # Ajoute l'abonné à la bibliothèque si l'entrée est valide
        if self.bibliotheque.ajouter_abonne(prenom, nom):
            self.afficher_message(f"Abonné {prenom} {nom} ajouté avec succès.")
        else:
            self.afficher_message("Abonné déjà existant.", "Erreur")

    def activer_supprimer_abonne(self):
        # Demande le prénom de l'abonné à supprimer
        prenom, ok1 = QInputDialog.getText(self, "Supprimer un abonné", "Entrez le prénom de l'abonné :")
        if not ok1:
            return

        # Demande le nom de l'abonné à supprimer
        nom, ok2 = QInputDialog.getText(self, "Supprimer un abonné", "Entrez le nom de l'abonné :")
        if not ok2:
            return

        # Supprime l'abonné de la bibliothèque
        self.bibliotheque.supprimer_abonne(prenom, nom)

    def activer_ajout_document(self):
        # Demande le type de document à ajouter
        classification, ok = QInputDialog.getItem(self, "Ajouter un document", "Entrez le type de document (Livre/Bande Dessinee) :",
                                                  ["Livre", "Bande Dessinee"], 0, False)
        if not ok:
            return

        # Vérifie que l'entrée est valide
        if classification.lower() != 'livre' and classification.lower() != 'bande dessinee':
            print("Type de document invalide.")
            return

        # Demande le titre et l'auteur du document
        titre, ok1 = QInputDialog.getText(self, "Ajouter un document", "Entrez le titre du document :")
        if not ok1:
            return

        auteur, ok2 = QInputDialog.getText(self, "Ajouter un document", "Entrez l'auteur :")
        if not ok2:
            return

        # Ajoute le document en fonction du type choisi
        if classification.lower() == 'livre':
            self.bibliotheque.ajouter_document(Livre(titre, auteur))
        elif classification.lower() == 'bande dessinee':
            # Demande le dessinateur si c'est une bande dessinée
            dessinateur, ok3 = QInputDialog.getText(self, "Ajouter une bande dessinée", "Entrez le dessinateur :")
            if not ok3:
                return
            self.bibliotheque.ajouter_document(BandeDessinee(titre, auteur, dessinateur))

    def activer_supprimer_document(self):
        # Demande le titre du document à supprimer
        titre, ok = QInputDialog.getText(self, "Supprimer un document", "Entrez le titre du document :")
        if not ok:
            return

        # Supprime le document de la bibliothèque
        self.bibliotheque.supprimer_document(titre)

    def activer_emprunt(self):
        # Permet à l'utilisateur d'emprunter un document
        identifiant = input("Entrez le titre ou l'ID du document : ")
        self.bibliotheque.emprunter_document(identifiant)

    def activer_retour(self):
        # Permet à l'utilisateur de retourner un document
        identifiant = input("Entrez le titre ou l'ID du document : ")
        self.bibliotheque.retourner_document(identifiant)

    def close(self):
        # Avant de fermer, on sauvegarde les données
        self.bibliotheque.sauvegarder_donnees()
        super().close()  # Appel à la méthode de fermeture de QWidget
