import json


class Serializable:
    """JSONを使って独自のシリアライズ表現を行う"""

    def __init__(self, *args) -> None:
        self.args = args

    def serialize(self):
        return json.dumps({"args": self.args})


class Point2D(Serializable):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point2D({self.x}, {self.y})"


class Deserializable(Serializable):
    """独自実装したSerializableをデシリアライズしてPoint2Dオブジェクトを構築する"""

    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params["args"])


class BetterPoint2D(Deserializable):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point2D({self.x}, {self.y})"


class BetterSerializable:
    def __init__(self, *args) -> None:
        self.args = args

    def serialize(self):
        return json.dumps(
            {
                "class": self.__class__.__name__,
                "args": self.args,
            }
        )

    def __repr__(self) -> str:
        name = self.__class__.__name__
        args_str = ",".join(str(x) for x in self.args)
        return f"{name}({args_str})"


registry = {}


def register_class(target_class):
    registry[target_class.__name__] = target_class


def deserialize(data):
    params = json.loads(data)
    name = params["class"]
    target_class = registry[name]
    return target_class(*params["args"])


class EvenBetterPoint2D(BetterSerializable):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.x = x
        self.y = y


register_class(EvenBetterPoint2D)  # 忘れがち


# regster_classの呼び出しが忘れがちになることを改善
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls


class RegisteredSerializable(BetterSerializable, metaclass=Meta):
    pass


class Vector3D(RegisteredSerializable):
    # __init__()と等価な役割を担う__init_subclass__()
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        register_class(cls)

    # def __init__(self, x, y, z) -> None:
    #     super().__init__(x, y, z)
    #     self.x, self.y, self.z = x, y, z


if __name__ == "__main__":
    point = Point2D(5, 3)
    print("Object ", point)
    print("Serialized ", point.serialize())
    print("-" * 10)

    # この実装ではシリアライズしたデータの型が事前にわかっていないと上手くいかない
    before = BetterPoint2D(5, 3)
    print("Before ", before)  # Before  Point2D(5, 3)
    data = before.serialize()
    print("Selialized ", data)  # Selialized  {"args": [5, 3]}
    after = BetterPoint2D.deserialize(data)
    print("After ", after)  # After  Point2D(5, 3)
    print("-" * 10)

    # シリアライズ実装の改善
    before = EvenBetterPoint2D(5, 3)
    print("Before ", before)  # Before  Point2D(5, 3)
    data = before.serialize()
    print("Selialized ", data)  # Selialized  {"args": [5, 3]}
    after = deserialize(data)
    print("After ", after)  # After  Point2D(5, 3)
    print("-" * 10)

    # register_class()を呼び出さなくてよくなった
    before = Vector3D(10, -7, 3)
    print("Before ", before)
    data = before.serialize()
    print("Selialized ", data)
    after = deserialize(data)
    print("After ", after)
