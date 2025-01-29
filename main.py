#Caroline Ceus-Dorphelus
#Félix-Antonin Noël
#Guillaume Pinat

"""
Classe abonnés:
Attributs:
identifiant
Prénom
Nom
-----
Classe Bibliothèque
Attributs:


Méthodes:
Ajouter abonné
Supprimer abonné
Afficher tout abonné
ajouter document
Supprimer document
Afficher tout document

Classe bibliothèque
Classe Documents

"""

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
import sys
from functools import partial


class Menu(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout() # QVBoxLayout permet d'empiler les boutons verticalement.

        self.boutons = [
            QPushButton("1 - Ajouter un abonné"),
            QPushButton("2 - Supprimer un abonné"),
            QPushButton("3 - Afficher tous les abonnés"),
            QPushButton("4 - Ajouter un document"),
            QPushButton("5 - Supprimer un document"),
            QPushButton("6 - Afficher tous les documents"),
            QPushButton("7 - Ajouter un emprunt"),
            QPushButton("8 - Retour d'un emprunt"),
            QPushButton("9 - Afficher tous les emprunts"),
            QPushButton("Q - Quitter")
        ]

        for i, bouton in enumerate(self.boutons): # Parcourt la liste des boutons tout en récupérant l'index (i) et l'objet bouton (bouton)
            layout.addWidget(bouton) # Ajout du bouton au layout
            bouton.clicked.connect(partial(self.active_choix, i + 1)) #CHAT GPT WAS HERE! Explication juste après
            """ 
            Dans PyQt, la méthode clicked.connect() ne permet pas de passer directement des arguments à une fonction.
            On utilise donc lambda ou functools.partial pour ajouter un paramètre à active_choix().
            
            Problème sans lambda ou partial :
            bouton.clicked.connect(self.active_choix(i + 1)) # Cette ligne exécuterait immédiatement self.active_choix(i + 1) au moment de la boucle, au lieu de l'attendre un clic et ce sera donc toujours le dernier index
                
            functools.partial est une fonction du module standard functools qui permet de préremplir certains arguments d'une fonction. Il retourne une nouvelle fonction avec ces arguments déjà fixés.
            C'est une alternative plus propre à lambda quand on doit passer des arguments à une fonction connectée à un signal PyQt.
            """

        # Ajout d'un champ de saisie pour la sélection par clavier
        self.saisie = QLineEdit() # Permet d'entrer un chiffre ou "Q/q" pour exécuter une action.
        self.saisie.setPlaceholderText("Entrez un chiffre (1-9) ou Q/q pour quitter")
        self.saisie.returnPressed.connect(self.cleanup)
        layout.addWidget(self.saisie)

        self.setLayout(layout)

    def cleanup(self):
        text = self.saisie.text().strip().lower() # Récupère le texte, enlève les espaces et convertit en minuscules
        self.saisie.clear()  # Efface le champ de saisie
        if text.isdigit(): # Si c'est un chiffre
            choix = int(text) # Convertit le texte en entier
            if 1 <= choix <= 9: # Si l'option est entre 1 et 9
                self.active_choix(choix) # Appelle la fonction active_choix avec l'option choisie
            else:
                print("Option invalide, veuillez entrer un chiffre entre 1 et 9.")  # Message d'erreur pour option invalide
        elif text.lower() == 'q':
            self.close() # Ferme la fenêtre
        else:
            print("Entrée invalide. Veuillez entrer un chiffre entre 1 et 9 ou 'Q' pour quitter.")  # Message pour entrée invalide

    def active_choix(self, choix):
        fonctions = {
            1: self.ajouter_abonne,
            2: self.supprimer_abonne,
            3: self.afficher_abonnes,
            4: self.ajouter_document,
            5: self.supprimer_document,
            6: self.afficher_documents,
            7: self.ajouter_emprunt,
            8: self.retour_emprunt,
            9: self.afficher_emprunts,
            10: self.close
        }
        fonctions[choix]()  # Appelle la fonction

class Abonnes:
    _compteur_id = 0  # Attribut de classe
    def __init__(self, prenom, nom):
        Abonnes._compteur_id += 1
        self._id = Abonnes._compteur_id  # Utiliser _id pour éviter le doublon avec la classe
        self.prenom = prenom
        self.nom = nom

    def get_id(self):
        return self._id  # Retourne l'ID unique de l'abonné

    def __str__(self):
        return f'{self.get_id()} {self.prenom} {self.nom}'

"""class bibliotheque(abonnes):
    def __init__(self):
                
class documents():
    id_ABONNE = 0
    def __init__(self, type, titre):
        Documents.id_ABONNE += 1
        
        self.id_ABONNE = Documents.id_ABONNE
        self.type
"""

"""a = Abonnes("Guillaume","Pinat")
b = Abonnes("Caroline","Ceus-Dorphelus")
print(a.get_id())
print(b.get_id())
print(a)"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec())