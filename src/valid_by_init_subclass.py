# メタクラスはインスタンス生成前の振る舞い
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        """__new__ method

        Args:
            meta (_type_): Meta Class
            name (_type_): Class Name
            bases (_type_): Base Class
            class_dict (_type_): cls.__dict__

        Returns:
            _type_: _description_
        """
        print(f"* Running {meta}.__new__ for {name}")
        print("Bases:", bases)
        print(class_dict)
        return type.__new__(meta, name, bases, class_dict)


class MyClass(metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


class MySubClass(MyClass):
    other = 567

    def bar(self):
        pass


class ValidatePolygon(type):
    """あらゆる種類の多角形を表すクラスの妥当性検証を行うメタクラス"""

    def __new__(meta, name, bases, class_dict):
        if bases:
            if class_dict["sides"] < 3:
                raise ValueError("Polygons need 3+ sides")
        return type.__new__(meta, name, bases, class_dict)


class Polygon(metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls) -> int:
        """内角の和を求める

        Returns:
            int: 内角の和
        """
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


class Rectangle(Polygon):
    sides = 4


class Nonagon(Polygon):
    sides = 9


# sides=2にするとプログラムがそもそも実行できない
# わざわざメタクラスを作るのはめんどくさい
# print("Before class")
# class Line(Polygon):
#     print("Before sides")
#     sides = 2
#     print("After sides")


# print("After class")
# Before class
# Before sides
# After sides
# Traceback (most recent call last):
#   File "/workspace/src/valid_by_init_subclass.py", line 73, in <module>
#     class Line(Polygon):
#   File "/workspace/src/valid_by_init_subclass.py", line 41, in __new__
#     raise ValueError("Polygons need 3+ sides")
# ValueError: Polygons need 3+ sides


class BetterPolygon:
    sides = None

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError("Polygons need 3+ sides")

    @classmethod
    def interior_angles(cls) -> int:
        """内角の和を求める

        Returns:
            int: 内角の和
        """
        return (cls.sides - 2) * 180


class Hexagon(BetterPolygon):
    sides = 6


class Filled:
    color = None

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        if cls.color not in ("red", "green", "blue"):
            raise ValueError("Fills need a valid color")


# __init_subclass__()による妥当性検証の場合は複数のメタクラスを持てる
class RedTriangle(Filled, Polygon):
    color = "red"
    sides = 3
