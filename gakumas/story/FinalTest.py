from typing import List, Any
import random
from math import ceil
from ..Chara import Chara
from ..data.card.Card import Card

class FinalTest:

    def __init__(self, chara: Chara):
        self.__chara__: Chara = chara
        self.__bonus__: List[float] = [0.0 for _ in range(3)]

        self.__turn__: int = 1

        self.__draw__   : List[Card] = []   # 手札
        self.__pile__   : List[Card] = []   # 山札
        self.__discard__: List[Card] = []   # 捨て札
        self.__exclude__: List[Card] = []   # 除外

        self.__score__   : int = 0
        self.__hp__      : int = 0
        self.__genki__   : int = 0
        self.__syutyu__  : int = 0
        self.__kocho__   : int = 0
        self.__zekkocho__: int = 0

    # @classmethod
    # def initialize(cls, chara: Chara):
    #     params: List[float] = list[float](chara.params.get_params())
    #     for param in params:
    #         param /= 100
    #         param *= 1.5
    #     bonus: List[float] = params
    #     return FinalTest(chara, bonus)

    def execution(self, chara: Chara):

        choose: int
        self.__start__(chara)
        
        while self.__turn__ > 0:

            self.__card_drow__()
            choose = self.__card_choose__()
            self.__calc_score__(choose, self.__chara__)
            self.__proc__()

            self.__turn__ -=1

    # private methods
    def __start__(self, chara: Chara) -> None:
        self.__pile__ = self.__chara__.cards.get_cards()

        for i in range(3):
            self.__bonus__[i] = chara.params.get_params()[i] / 100 * 1.5

    def __card_drow__(self) -> None:
        print(f"\n< 残りターン: {self.__turn__} >")
        self.__draw__ = random.sample(self.__pile__, 3)   # TODO 1枚ずつピック
        for card in self.__draw__:
            self.__pile__.remove(card)
        for i in range(len(self.__draw__)):
            print(f"{i} : {self.__draw__[i].get_name()}")

    def __card_choose__(self) -> int:
        num: int
        num = int(input("choose 0-2? > "))
        # num = random.choice(range(3))
        return num
    
    def __calc_score__(self, num: int, chara: Chara) -> None:

        status: List[Any] = self.__draw__[num].get_status()

        self.__hp__       += status[1]
        self.__genki__    += status[2]
        self.__syutyu__   += status[3]
        self.__kocho__    += status[4]
        self.__zekkocho__ += status[5]
        self.__score__    += ceil(status[0] * self.__bonus__[0])  #TODO vodaviターンを判別

    def __proc__(self) -> None:
        # 1回のみの札は除外へ、それ以外は捨て札へ
        for card in self.__draw__:
            if card.get_status()[-1]:
                self.__exclude__.append(card)
            else:
                self.__discard__.append(card)

        self.__draw__ = []

    # public methods
    def get_score(self) -> int:
        return self.__score__

    def __del__(self):
        pass
