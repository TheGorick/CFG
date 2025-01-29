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

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit#, QInputDialog
import sys
from functools import partial

class Abonnes:
    _compteur_id = 0  # Attribut de classe

    def __init__(self, prenom, nom):
        Abonnes._compteur_id += 1
        self._id = Abonnes._compteur_id  # Utiliser _id pour éviter le doublon avec la classe
        self.prenom = prenom
        self.nom = nom

    def __str__(self):
        return f'{self.get_id()} {self.prenom} {self.nom}'

    # getters
    def get_id(self):
        return self._id

    def get_prenom(self):
        return self.prenom

    def get_nom(self):
        return self.nom

    # setters
    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_nom(self, nom):
        self.nom = nom

class Documents:
    _compteur_id = 0  # Attribut de classe

    def __init__(self, sorte, titre, disponible = True):
        Documents._compteur_id += 1
        self._id = Documents._compteur_id  # Utiliser _id pour éviter le doublon avec la classe
        self.sorte = sorte
        self.titre = titre
        self.disponible = disponible

    def __str__(self):
        return f'{self.get_id()} {self.sorte} {self.titre} {self.disponible}'

    # getters
    def get_id(self):
        return self._id

    def get_sorte(self):
        return self.sorte

    def get_titre(self):
        return self.titre

    def get_disponible(self):
        return self.disponible

    # setters
    def set_sorte(self, sorte):
        self.sorte = sorte

    def set_titre(self, titre):
        self.titre = titre

    def set_disponible(self, disponible):
        self.disponible = disponible

    def changer_disponible(self):
        self.disponible = not self.disponible
        if self.disponible:
            print(f"Le document '{self.titre}' est maintenant disponible.")
        else:
            print(f"Le document '{self.titre}' n'est plus disponible.")

class Bibliotheque:
    def __init__(self):
        self.abonnes = []  # Liste des abonnés
        self.documents = []  # Liste des documents
        self.emprunts = []

    # abonnées
    def ajouter_abonne(self, prenom, nom):
        for abonne in self.abonnes:
            if abonne.prenom == prenom and abonne.nom == nom:
                return False  # Abonné déjà existant
        self.abonnes.append(Abonnes(prenom, nom))
        return True

    def supprimer_abonne(self, prenom, nom):
        for abonne in self.abonnes:
            if abonne.prenom == prenom and abonne.nom == nom:
                self.abonnes.remove(abonne)
                return True
        return False  # Abonné introuvable

    def afficher_abonnes(self):
        if not self.abonnes:
            print("Aucun abonné enregistré.")
        for abonne in self.abonnes:
            print(abonne)

    # documents
    def ajouter_document(self, sorte, titre):
        for doc in self.documents:
            if doc.titre == titre:
                return False  # Document déjà existant
        self.documents.append(Documents(sorte, titre))
        return True

    def supprimer_document(self, titre):
        for doc in self.documents:
            if doc.titre == titre:
                self.documents.remove(doc)
                return True
        return False  # Document introuvable

    def afficher_documents(self):
        if not self.documents:
            print("Aucun document enregistré.")
        for doc in self.documents:
            print(doc)

    # emprunts
    def retour(self, identifiant):
        # Cherche le document par titre ou ID
        for doc in self.documents:
            if doc.get_titre() == identifiant or str(doc.get_id()) == identifiant:
                doc.changer_disponible()
                return True  # Statut changé
        return False  # Document non trouvé

    def afficher_emprunts(self):
        documents_non_disponibles = [doc for doc in self.documents if not doc.get_disponible()]
        if not documents_non_disponibles:
            print("Aucun document indisponible.")
        else:
            for doc in documents_non_disponibles:
                print(doc)

class Menu(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 300, 400)
        self.bibliotheque = Bibliotheque()

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
        if self.bibliotheque.ajouter_abonne(prenom, nom):
            print("Abonné ajouté avec succès.")
        else:
            print("L'abonné existe déjà.")

    def activer_supprimer_abonne(self):
        prenom = input("Entrez le prénom de l'abonné : ")
        nom = input("Entrez le nom de l'abonné : ")
        if self.bibliotheque.supprimer_abonne(prenom, nom):
            print("Abonné supprimer avec succès.")
        else:
            print("L'abonné n'existe pas.")

    def activer_ajout_document(self):
        sorte = input("Entrez le type de document : ")
        titre = input("Entrez le titre du document : ")
        if self.bibliotheque.ajouter_document(sorte, titre):
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec())