from typing import List
from ..data.card.Card import Card

class Cards:

    def __init__(self) -> None:
        self.__inventory__: List[Card] = []

    def add_card(self, card: Card):
        self.__inventory__.append(card)

    # getter methods
    def get_cards(self) -> List[Card]:
        return self.__inventory__

    def __del__(self) -> None:
        pass
