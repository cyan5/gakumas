from .Chara import Chara
from .story.FinalTest import FinalTest
from .data.card.Card import Card

class Story:
    
    def __init__(self, grade: str):
        self.__grade__: str = grade
        self.__chara__: Chara = Chara("Saki", "SSR1")

        self.finaltest: FinalTest = FinalTest(self.__chara__)

    def execution(self):

        self.__chara__.params.set_params(100, 100, 100)

        card1: Card = Card("アピール")
        card2: Card = Card("集中")
        card3: Card = Card("基本")
        self.__chara__.cards.add_card(card1)
        self.__chara__.cards.add_card(card2)
        self.__chara__.cards.add_card(card3)

        self.finaltest.execution(self.__chara__)
        print(f"\nfinal test score: {self.finaltest.get_score()}")

    def __del__(self):
        pass
