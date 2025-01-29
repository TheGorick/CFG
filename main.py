#Caroline Ceus-Dorphelus
#Félix-Antonin Noël
#Guillaume Pinat

import Menu as Menu
from PyQt6.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Menu.Menu()
    window.show()
    sys.exit(app.exec())