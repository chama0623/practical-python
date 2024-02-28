from typing import Type


# example of diamond problem(ダイヤモンド継承)
# Aを継承したB, Cがあり, BとCを2重継承したDがある. B, CがAのメソッドをそれぞれ
# オーバーライドしているとき, DではB, Cどちらのメソッドが継承されるか?
class MyBaseClass:
    """Base Class(class A)"""

    def __init__(self, value: int) -> None:
        self.value = value


class TimesSeven(MyBaseClass):
    """Times Seven Class(class B)"""

    def __init__(self, value: int) -> None:
        super().__init__(value)
        self.value *= 7


class PlusNine(MyBaseClass):
    """Plus Nine Class(class C)"""

    def __init__(self, value: int) -> None:
        super().__init__(value)
        self.value += 9


class GoodWay1(TimesSeven, PlusNine):
    """Class D
    (value + 9) * 7
    """

    def __init__(self, value: int) -> None:
        super().__init__(value)


class GoodWay2(PlusNine, TimesSeven):
    """Class D
    (value * 7) + 9
    """

    def __init__(self, value: int) -> None:
        super().__init__(value)


def get_mro(cls: Type) -> str:
    """get Method Resolution Order(MRO) infomation by strings

    Args:
        cls (Callable): Class to get MRO infomation

    Returns:
        str: MRO infomation
    """
    return "\n".join(repr(c) for c in cls.mro())


if __name__ == "__main__":
    # __init_の実行順は標準メソッド解決手順(MRO;Method Resolution Order)による
    foo = GoodWay1(5)
    mro_str = get_mro(GoodWay1)
    print(f"(5 + 9) * 7 = {foo.value}")  # -> 98
    print(mro_str)
    # GoodWay1がTimesSevenを呼び出し, そのTimesSevenがPlusNineを呼び出す.
    # このため(value + 9) * 7 = 98がvalueの値になる
    # <class '__main__.GoodWay1'>
    # <class '__main__.TimesSeven'>
    # <class '__main__.PlusNine'>
    # <class '__main__.MyBaseClass'>
    # <class 'object'>

    bar = GoodWay2(5)
    mro_str = get_mro(GoodWay2)
    print(f"(5 * 7) + 9 = {bar.value}")  # -> 44
    print(mro_str)
    # <class '__main__.GoodWay2'>
    # <class '__main__.PlusNine'>
    # <class '__main__.TimesSeven'>
    # <class '__main__.MyBaseClass'>
    # <class 'object'>
