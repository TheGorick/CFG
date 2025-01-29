import Documents as Documents, Abonnes as Abonnes

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
        self.abonnes.append(Abonnes.Abonnes(prenom, nom))
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
        self.documents.append(Documents.Documents(sorte, titre))
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
            print("Aucun document emprunté.")
        else:
            for doc in documents_non_disponibles:
                print(doc)