class Abonnes:
    _compteur_id = 0  # Attribut de classe

    def __init__(self, prenom, nom, mail):
        Abonnes._compteur_id += 1
        self._id = Abonnes._compteur_id  # Utiliser _id pour éviter le doublon avec la classe
        self.prenom = prenom
        self.nom = nom
        self.mail = mail

    def __str__(self):
        return f'{self.get_id()} {self.prenom} {self.nom} {self.mail}'

    # getters
    def get_id(self):
        return self._id

    def get_prenom(self):
        return self.prenom

    def get_nom(self):
        return self.nom

    def get_mail(self):
        return self.mail

    # setters
    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_nom(self, nom):
        self.nom = nom

    def set_mail(self, mail):
        self.mail = mail