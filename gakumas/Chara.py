from typing import List
from .chara.Params import Params
# from chara.Drinks import Drinks
from .chara.Cards import Cards

class Chara:

    def __init__(self, name: str, rarity: str):
        self.name: str = name
        self.rarity: str = rarity

        # classes
        # self.hp = HP()
        self.params = Params(0, 0, 0)
        # self.drinks = Drinks()
        self.cards = Cards()

    # getter methods
    def get_name(self) -> str:
        return self.name

    def __del__(self):
        del self.params
        del self.cards
