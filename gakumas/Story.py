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

        self.chara.cards.add_card(Card("アピール"))
        self.chara.cards.add_card(Card("アピール"))
        self.chara.cards.add_card(Card("アピール"))
        self.chara.cards.add_card(Card("アピール"))
        self.chara.cards.add_card(Card("集中"))
        self.chara.cards.add_card(Card("集中"))
        self.chara.cards.add_card(Card("集中"))
        self.chara.cards.add_card(Card("集中"))
        self.chara.cards.add_card(Card("基本"))
        self.chara.cards.add_card(Card("基本"))
        self.chara.cards.add_card(Card("基本"))
        self.chara.cards.add_card(Card("基本"))

        # story
        self.finaltest.start(self.chara.params.get_params(), self.chara.hp.get_hp(), self.chara.cards.get_cards())
        self.finaltest.execution()

    def __del__(self):
        del self.chara
        del self.finaltest

