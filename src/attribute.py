class MyObject:
    def __init__(self) -> None:
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self) -> int:
        """Get private field

        Returns:
            int: self.__private_field
        """
        return self.__private_field


class MyParentObject:
    def __init__(self) -> None:
        self.__private_field = 71


class MyChildObject(MyParentObject):
    def get_private_field(self) -> int:
        """Get private field

        Returns:
            int: self.__private_field
        """
        return self.__private_field


if __name__ == "__main__":
    foo = MyObject()
    print(foo.public_field)
    print(foo.get_private_field())
    # print(foo.__private_field)
    # -> AttributeError: 'MyObject' object has no attribute '__private_field'.
    # Did you mean: 'get_private_field'?

    bar = MyChildObject()
    # print(bar.get_private_field())
    # サブクラスからスーパークラスのプライベートフィールドにアクセスできない
    # -> AttributeError: 'MyChildObject' object has no attribute '_MyChildObject__private_field'.
    # Did you mean: '_MyParentObject__private_field'?

    # プライベートフィールドは属性名の単純な変換で実装されている.
    # 例えばMyParent.__private_fieldは_MyParentObject__private_fieldに変換されている.
    # なので_MyParentObject__private_fieldを呼び出せばプライベート属性にアクセスできる
    print(bar._MyParentObject__private_field)  # barはMychildObjectクラス
    print(bar.__dict__)  # __dict__でもこれが見られる

    # _value : プライベート属性であることを明示する(別にプライベートではない)
    # __value : 名前衝突を回避するために使用する
