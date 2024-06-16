from typing import List

class Card:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.data: dict = {
            # パラメータ、体力、元気、集中、好調、絶好調、1回のみ
            "アピール": [ 9, -4,  0,  0,  0,  0, False], 
            "集中"    : [ 0, -2,  1,  2,  0,  0, False], 
            "基本"    : [ 0,  0,  4,  0,  0,  0, True ], 
        }

    # getter methods
    def get_name(self) -> str:
        return self.name
    
    def get_status(self) -> List[int]:
        return self.data[self.name]

    def __del__(self) -> None:
        pass
