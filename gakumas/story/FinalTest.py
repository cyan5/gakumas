from ..Chara import Chara
from ..data.card.Card import Card
from .Status import TestStatus

from typing import List
import random

class FinalTest:

    def __init__(self):

        self.status: TestStatus
        self.turn_type_list: List[int]

        self.turn: int = 12

        self.draw   : List[Card] = []   # 手札
        self.pile   : List[Card] = []   # 山札
        self.discard: List[Card] = []   # 捨て札
        self.exclude: List[Card] = []   # 除外

    def start(self, params: List[int], hp: int, cards: List[Card]):
        self.status = TestStatus(params, hp)
        self.turn_type_list = [0, 2, 1, 1, 2, 2, 1, 1, 0, 2, 0, 1]  # vo: 0,  da: 1, vi: 2

        for card in cards:
            self.pile.append(card)

    def execution(self):
        while self.turn > 0:
            
            self._card_drow()
            chosen_card: int = self._card_choose()
            self._calc_score(chosen_card, self.turn_type_list[self.turn])
            self._chosen_card_proc(chosen_card)
            self._card_proc()

            self.turn -=1

        print(f"\nfinal test score: {self.status.get_score()}")

    # private methods
    def _card_drow(self) -> None:
        print(f"\n< 残りターン: {self.turn} >")
        # self.draw = random.sample(self.pile, 3)   # TODO 1枚ずつピック
        for _ in range(3):
            
            if len(self.pile) == 0:
                for card in self.discard:
                    self.pile.append(card)
                self.discard = []
            
            choice: Card = random.choice(self.pile)
            self.draw.append(choice)
            self.pile.remove(choice)

        for i in range(len(self.draw)):
            print(f"{i} : {self.draw[i].get_name()}")

    def _card_choose(self) -> int:
        num: int
        num = int(input("choose 0-2? > "))
        # num = random.choice(range(3))
        return num
    
    def _calc_score(self, choose_num: int, turn_type: int) -> None:
        self.draw[choose_num].operation(self.status, turn_type)

    def _chosen_card_proc(self, chosen_card: int) -> None:
        card: Card = self.draw[chosen_card]
        if card.is_onlyone():
            self.exclude.append(card)
        else:
            self.discard.append(card)
        self.draw.remove(card)

    def _card_proc(self) -> None:
        self.status.proc(self.turn_type_list[self.turn])

        for card in self.draw:
            self.discard.append(card)
        self.draw = []

    def __del__(self):
        del self.status

