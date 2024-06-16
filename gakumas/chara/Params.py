from typing import List

class Params:

    def __init__(self, vo: int, da: int, vi: int) -> None:
        self.params: List[int] = [vo, da, vi]

    # public methos
    def add_params(self, vo: int, da: int, vi: int):
        self.params += [vo, da, vi]

    # setter methods
    def set_params(self, vo: int, da: int, vi: int) -> None:
        self.params = [vo, da, vi]

    # getter_methods
    def get_params(self) -> List[int]:
        return self.params

    def __del__(self) -> None:
        pass
