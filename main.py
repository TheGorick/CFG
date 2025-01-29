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
import Menu as Menu
from PyQt6.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Menu.Menu()
    window.show()
    sys.exit(app.exec())