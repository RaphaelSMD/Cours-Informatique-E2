import random

class CardValue:
    def __init__(self, value_txt: str, value_pts: int):
        self.value_txt = value_txt
        self.value_pts = value_pts

class CardColor :
    def __init__(self, shade: str, shade_name: str, foreground_color: str, background_color: str):
        self.shade = shade
        self.shade_name = shade_name
        self.foreground_color = foreground_color
        self.background_color = background_color

class Card :
    def __init__(self, value: CardValue, color: CardColor):
        self.value = value
        self.color = color

    def __str__(self):
        return f"{self.value.value_txt} of {self.color.shade_name}"

    def is_equal_value(self, card : 'Card'):
        return self.value.value_pts == card.value.value_pts

    def __eq__(self, card : 'Card'):
        return self.value.value_pts == card.value.value_pts and self.color.shade == card.color.shade

    def __ne__(self, card : 'Card'):
        return not self == card

    def __gt__(self, card : 'Card'):
        return self.value.value_pts > card.value.value_pts

    def __lt__(self, card : 'Card'):
        return self.value.value_pts < card.value.value_pts

    def __ge__(self, card : 'Card'):
        return self.value.value_pts >= card.value.value_pts

    def __le__(self, card : 'Card'):
        return self.value.value_pts <= card.value.value_pts

    def __repr__(self) -> str:
        return f"Card({self.value.value_txt}, {self.color.shade_name})"

__name__ = "__main__"
couleurs = [
    CardColor("♠", "Pique", "Noir", "Blanc"),
    CardColor("♣", "Trèfle", "Noir", "Blanc"),
    CardColor("♦", "Carreau", "Rouge", "Blanc"),
    CardColor("♥", "Coeur", "Rouge", "Blanc")
]
valeurs = [
    CardValue("2", 2), CardValue("3", 3), CardValue("4", 4),
    CardValue("5", 5), CardValue("6", 6), CardValue("7", 7),
    CardValue("8", 8), CardValue("9", 9), CardValue("10", 10),
    CardValue("J", 11), CardValue("Q", 12), CardValue("K", 13), CardValue("A", 14)
]
carte1 = Card(random.choice(valeurs), random.choice(couleurs))
carte2 = Card(random.choice(valeurs), random.choice(couleurs))

print(f"Carte 1 tirée : {carte1}")
print(f"Carte 2 tirée : {carte2}\n")

if carte1 > carte2:
    print(f"{carte1} est plus forte que {carte2}")
elif carte1 < carte2:
    print(f"{carte2} est plus forte que {carte1}")
else:
    print(f"{carte1} et {carte2} ont la même valeur !")