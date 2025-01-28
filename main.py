#Caroline Ceus-Dorphelus
#Félix-Antonin Noël
#Guillaume Pinat

"""
•		
*1 Ajouter abonné
*2 Supprimer abonné
*3 Afficher tous les abonnés
*4 Ajouter Document
*5 Supprimer Document
*6 Afficher tous les Documents
*7 Ajouter Emprunts
*8 Retour d’un Emprunts
*9 Afficher tous les Emprunts
*Q Quitter
"""

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


class Abonnes:
    __id_Abonne = 0
    def __init__(self,prenom, nom):
        Abonnes.__id_Abonne += 1
        self.__id_Abonne = Abonnes.__id_Abonne
        self.prenom = prenom
        self.nom = nom

    def get_id(self):
        return self.__id_Abonne

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

a = Abonnes("Guillaume","Pinat")
b = Abonnes("Caroline","Ceus-Dorphelus")
print(a.get_id())
print(b.get_id())
print(a)