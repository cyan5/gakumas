from typing import List
from math import ceil

class _Status:

    def __init__(self, params: List[int], hp: int):
        self.score: int = 0
        self.bonus: List[float] = [0.0 for _ in range(3)]
        for i in range(3):
            self.bonus[i] = params[i] / 100 * 1.5

        self.param   : int = 0
        # 共通ステータス
        self.hp      : int = hp
        self.genki   : int = 0
        # センス
        self.syutyu  : int = 0
        self.kocho   : int = 0
        self.zekkocho: int = 0
        # ロジック
        self.yaruki  : int = 0
        self.koinsho : int = 0

        # 減少フラグ
        self.dec_kocho   : bool = False
        self.dec_zekkocho: bool = False
        self.dec_koinsho : bool = False

    # adder methods
    def add_param(self, num) -> None:
        kocho_scale: float = 1.0
        if self.kocho >= 1:
            kocho_scale = 1.5
        if self.zekkocho >= 1:
            kocho_scale += self.kocho * 0.1
        
        self.param = ceil((num + self.syutyu) * kocho_scale)

    def add_hp(self, num: int) -> None:
        self.hp += num

    def add_genki(self, num: int) -> None:
        self.genki += self.yaruki + num

    def add_syutyu(self, num: int) -> None:
        self.syutyu += num

    def add_kocho(self, num: int) -> None:
        self.kocho += num

    def add_zekkocho(self, num: int) -> None:
        self.zekkocho += num

    def add_yaruki(self, num: int) -> None:
        self.yaruki += num

    # private_method

    # proc
    def _proc(self) -> None:

        if self.kocho >= 1:
            self.dec_kocho = True
        if self.dec_kocho:
            self.kocho -= 1
        if self.kocho == 0:
            self.dec_kocho = False

        if self.zekkocho >= 1:
            self.dec_zekkocho = True
        if self.dec_zekkocho:
            self.zekkocho -= 1
        if self.zekkocho == 0:
            self.dec_zekkocho = False

        if self.koinsho >= 1:
            self.dec_koinsho = True
        if self.dec_koinsho:
            self.koinsho -= 1
        if self.koinsho == 0:
            self.dec_koinsho = False

    def get_score(self) -> int:
        return self.score

    def __del__(self):
        pass

class LessonStatus(_Status):
    def proc(self, turn_type) -> None:
        self.param = self.koinsho
        self.score += self.param
        _Status._proc(self)

    def add_param(self, num: int, turn_type: int) -> None:
        _Status.add_param(self, num)
        self.score += self.param

class TestStatus(_Status):
    def proc(self, turn_type) -> None:
        self.param = self.koinsho
        self.score += ceil(self.param * self.bonus[turn_type])
        _Status._proc(self)

    def add_param(self, num: int, turn_type: int) -> None:
        _Status.add_param(self, num)
        self.score += ceil(self.param * self.bonus[turn_type])
