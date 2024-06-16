from typing import List, Any
import random
from math import ceil
from ..Chara import Chara
from ..data.card.Card import Card

class FinalTest:

    def __init__(self):
        self.bonus: List[float] = [0.0 for _ in range(3)]

        self.turn: int = 1

        self.draw   : List[Card] = []   # 手札
        self.pile   : List[Card] = []   # 山札
        self.discard: List[Card] = []   # 捨て札
        self.exclude: List[Card] = []   # 除外

        self.score   : int = 0
        self.hp      : int = 0
        self.genki   : int = 0
        self.syutyu  : int = 0
        self.kocho   : int = 0
        self.zekkocho: int = 0

    def execution(self, chara: Chara):

        self._start(chara)
        while self.turn > 0:

            self._card_drow()
            self._calc_score(self._card_choose(), chara)
            self._proc()

            self.turn -=1

        print(f"\nfinal test score: {self.score}")

    # private methods
    def _start(self, chara: Chara) -> None:
        self.pile = chara.cards.get_cards()

        for i in range(3):
            self.bonus[i] = chara.params.get_params()[i] / 100 * 1.5

    def _card_drow(self) -> None:
        print(f"\n< 残りターン: {self.turn} >")
        self.draw = random.sample(self.pile, 3)   # TODO 1枚ずつピック
        for card in self.draw:
            self.pile.remove(card)
        for i in range(len(self.draw)):
            print(f"{i} : {self.draw[i].get_name()}")

    def _card_choose(self) -> int:
        num: int
        num = int(input("choose 0-2? > "))
        # num = random.choice(range(3))
        return num
    
    def _calc_score(self, num: int, chara: Chara) -> None:
        status: List[Any] = self.draw[num].get_status()

        self.hp       += status[1]
        self.genki    += status[2]
        self.syutyu   += status[3]
        self.kocho    += status[4]
        self.zekkocho += status[5]
        self.score    += ceil(status[0] * self.bonus[0])  #TODO vodaviターンを判別

    def _proc(self) -> None:
        # 1回のみの札は除外へ、それ以外は捨て札へ
        for card in self.draw:
            if card.get_status()[-1]:
                self.exclude.append(card)
            else:
                self.discard.append(card)

        self.draw = []

    # getter methods
    def get_score(self) -> int:
        return self.score

    def __del__(self):
        pass
