

class HP:

    def __init__(self):
        self.hp: int = 31

    def add_hp(self, score: int) -> None:
        self.hp += score

    # setter method
    def set_hp(self, score: int) -> None:
        self.hp = score

    # getter method
    def get_hp(self) -> int:
        return self.hp

    def __del__(self):
        pass
