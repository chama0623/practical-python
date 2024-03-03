class Field:
    def __init__(self, name: str) -> None:
        self.name = name
        self.internal_name = "_" + self.name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, "")

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Customer:
    # この定義の仕方は冗長でめんどくさい
    first_name = Field("first_name")
    second_name = Field("second_name")
    prefix = Field("prefix")
    suffix = Field("suffix")


class Field2:
    def __init__(self) -> None:
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, "")

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field2):
                value.name = key
                value.internal_name = "_" + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


class DatabaseRow(object, metaclass=Meta):
    pass


# DatabaseRowを継承しないといけない
class BetterCustomer(DatabaseRow):
    first_name = Field2()
    second_name = Field2()
    prefix = Field2()
    suffix = Field2()


class Field3:
    def __init__(self) -> None:
        self.name = None
        self.internal_name = None

    def __set_name__(self, owner, name):
        # クラス作成時に各ディスクリプタに呼ばれる
        self.name = name
        self.internal_name = "_" + name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, "")

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


# DatabaseRowを継承しなくてもいい
class FixedCustomer:
    first_name = Field3()
    second_name = Field3()
    prefix = Field3()
    suffix = Field3()


if __name__ == "__main__":
    cust = FixedCustomer()
    print(f"Before: {cust.first_name!r} {cust.__dict__}")
    cust.first_name = "Euclid"
    print(f"After : {cust.first_name!r} {cust.__dict__}")
