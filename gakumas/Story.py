from .Chara import Chara
from .story.FinalTest import FinalTest
from .data.card.Card import Card

class Story:

    def __init__(self, grade: str):
        self.grade: str = grade

        # classes
        self.chara: Chara = Chara("Saki", "SSR1")
        self.finaltest: FinalTest = FinalTest()

    def execution(self):

        self.chara.params.set_params(100, 100, 100)

        card1: Card = Card("アピール")
        card2: Card = Card("集中")
        card3: Card = Card("基本")
        self.chara.cards.add_card(card1)
        self.chara.cards.add_card(card2)
        self.chara.cards.add_card(card3)

        # story
        self.finaltest.execution(self.chara)

    def __del__(self):
        del self.chara
        del self.finaltest

