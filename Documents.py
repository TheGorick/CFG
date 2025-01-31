#Caroline Ceus-Dorphelus
#Félix-Antonin Noël
#Guillaume Pinat

class Documents:
    _compteur_id = 0  # Attribut de classe

    def __init__(self, classification, titre, disponibilite = True):
        Documents._compteur_id += 1
        self._id = Documents._compteur_id  # Utiliser _id pour éviter le doublon avec la classe
        self.classification = classification
        self.titre = titre
        self.disponibilite = disponibilite

    def __str__(self):
        return f'{self.get_id()} {self.classification} {self.titre} {self.disponibilite}'

    # getters
    def get_id(self):
        return self._id

    def get_classification(self):
        return self.classification

    def get_titre(self):
        return self.titre

    def get_disponibilite(self):
        return self.disponibilite

    # setters
    def set_classification(self, classification):
        self.classification = classification

    def set_titre(self, titre):
        self.titre = titre

    def set_disponibilite(self, disponibilite):
        self.disponibilite = disponibilite

    def changer_disponibilite(self):
        self.disponibilite = not self.disponibilite
        if self.disponibilite:
            print(f"Le document '{self.titre}' est maintenant disponible.")
        else:
            print(f"Le document '{self.titre}' n'est plus disponible.")