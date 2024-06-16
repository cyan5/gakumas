from typing import List
from ..data.card.Card import Card

class Cards:

    def __init__(self) -> None:
        self.inventory: List[Card] = []

    def add_card(self, card: Card):
        self.inventory.append(card)

    # getter methods
    def get_cards(self) -> List[Card]:
        return self.inventory

    def __del__(self) -> None:
        pass
