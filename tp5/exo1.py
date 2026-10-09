class Rectangle:

    def __init__(self, longueur=0, largeur=0):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = "rectangle"

    def surface(self):
        return self.longueur * self.largeur

    def afficher(self):
        print(
            f"Nom : {self.nom}, Longueur : {self.longueur}, Largeur : {self.largeur}, Surface : {self.surface()}"
        )

class Carre(Rectangle):

    def __init__(self, cote=0):
        super().__init__(longueur=cote, largeur=cote)
        self.nom = "carré"

if __name__ == "__main__":
    r = Rectangle(longueur=5, largeur=3)
    c = Carre(cote=4)

    r.afficher()
    c.afficher()