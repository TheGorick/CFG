#Caroline Ceus-Dorphelus
#Félix-Antonin Noël
#Guillaume Pinat

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