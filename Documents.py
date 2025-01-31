#Caroline Ceus-Dorphelus
#Félix-Antonin Noël
#Guillaume Pinat

class Documents:
    _compteur_id = 0  # Attribut de classe

    def __init__(self, classification, titre, dispo = True):
        Documents._compteur_id += 1
        self._id = Documents._compteur_id  # Utiliser _id pour éviter le doublon avec la classe
        self.classification = classification
        self.titre = titre
        self.dispo = dispo

    def __str__(self):
        return f'ID: {self.get_id()} Type: {self.classification} Titre: {self.titre} Disponible: {"Oui" if self.dispo else "Non"}'

    # getters
    def get_id(self):
        return self._id

    def get_classification(self):
        return self.classification

    def get_titre(self):
        return self.titre

    def get_dispo(self):
        return self.dispo

    # setters
    def set_classification(self, classification):
        self.classification = classification

    def set_titre(self, titre):
        self.titre = titre

    def set_dispo(self, dispo):
        self.dispo = dispo

    def changer_dispo(self):
        self.dispo = not self.dispo
        if self.dispo:
            print(f"Retour de '{self.titre}'.")
        else:
            print(f"Emprunt de '{self.titre}'.")