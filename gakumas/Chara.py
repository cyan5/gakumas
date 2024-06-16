from typing import List
from .chara.Params import Params
# from chara.Drinks import Drinks
from .chara.Cards import Cards

class Chara:
    def __init__(self, name: str, rarity: str):
        self.__name__: str = name
        self.__rarity__: str = rarity

        # classes
        self.params = Params(0, 0, 0)
        # self.__drinks__ = Drinks()
        self.cards = Cards()
        # self.__hp__ = HP()

    # getter methods
    def get_name(self) -> str:
        return self.__name__

    def __del__(self):
        del self.params
        del self.cards
