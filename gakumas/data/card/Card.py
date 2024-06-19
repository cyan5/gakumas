from ...story.Status import TestStatus

from typing import List

class Card:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.onlyone: bool

        onlyone_str: str = "基本"
        if name in onlyone_str:
            self.onlyone = True
        else:
            self.onlyone = False

    def is_choosable(self, score: int, turn: int) -> bool:
        return True

    def operation(self, status: TestStatus, turn_type: int) -> None:
        if self.name == "アピール":

            status.add_hp(-4)
            status.add_param(9, turn_type)

        elif self.name == "基本":

            status.add_genki(4)

        elif self.name == "集中":

            status.add_hp(-1)
            status.add_genki(1)
            status.add_syutyu(2)

    def is_onlyone(self) -> bool:
        return self.onlyone

    # getter methods
    def get_name(self) -> str:
        return self.name
    
    def __del__(self) -> None:
        pass
