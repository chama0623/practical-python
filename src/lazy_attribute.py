from typing import Any


class LazyRecord:
    def __init__(self) -> None:
        self.exists = 5

    def __getattr__(self, name):
        value = f"Value for {name}"
        setattr(self, name, value)
        return value


class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f"* Called __getattr__({name!r})," f"populating instance dictionary")
        result = super().__getattr__(name)
        print(f"Returning {result!r}")
        return result


class ValidatingRecord:
    def __init__(self) -> None:
        self.exists = 5

    def __getattribute__(self, name: str) -> Any:
        print(f"* Called __getattr__({name!r})," f"populating instance dictionary")
        try:
            value = super().__getattribute__(name)
            print(f"* Found {name!r}, returning {value!r}")
            return value
        except AttributeError:
            value = f"Value for {name}"
            print(f"* Setting {name!r} to {value!r}")
            setattr(self, name, value)
            return value


class SavingRecord:
    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)


class LoggingSavingRecord(SavingRecord):
    def __setattr__(self, name: str, value: Any) -> None:
        print(f"Called __setattr__({name!r}, {value!r})")
        return super().__setattr__(name, value)


if __name__ == "__main__":
    data = LazyRecord()
    # data.fooを呼び出すとインスタンス辞書にないため__getattr__()が呼び出される
    print("Before:", data.__dict__)  # Before: {'exists': 5}
    print("foo   :", data.foo)  # foo   : Value for foo
    print("After  :", data.__dict__)  # After  : {'exists': 5, 'foo': 'Value for foo'}
    print("-" * 10)

    # __getattr__()の呼び出しを見てみる
    data = LoggingLazyRecord()
    print("exists    :", data.exists)  # exists    : 5
    print("First foo :", data.foo)
    # * Called __getattr__('foo'),populating instance dictionary
    # Returning 'Value for foo'
    # First foo : Value for foo
    print("Second foo:", data.foo)  # Second foo: Value for foo
    # この振る舞いを応用すると, データがない場合はデータベースから取得し,
    # データがある場合にはそのデータを返すという処理を実装できる
    print("-" * 10)

    # __getattribute__()を使うとトランザクションの振る舞いも行える
    # 次にアクセスしたときに有効なデータを持っているか確かめる
    data = ValidatingRecord()
    print("exists    :", data.exists)
    # * Called __getattr__('exists'),populating instance dictionary
    # * Found 'exists', returning 5
    # exists    : 5
    print("First foo :", data.foo)
    # * Called __getattr__('foo'),populating instance dictionary
    # * Setting 'foo' to 'Value for foo'
    # First foo : Value for foo
    print("Second foo:", data.foo)
    # * Called __getattr__('foo'),populating instance dictionary
    # * Found 'foo', returning 'Value for foo'
    # Second foo: Value for foo
    print("-" * 10)

    # __setattr__()でオブジェクトに値が代入されたときにデータベースに遅延的に値を戻す
    data = LoggingSavingRecord()
    print("Before :", data.__dict__)  # Before : {}
    data.foo = 5
    print("After  :", data.__dict__)
    # Called __setattr__('foo', 5)
    # After  : {'foo': 5}
    data.foo = 7
    # Called __setattr__('foo', 7)
    # Finally: {'foo': 7}
    print("Finally:", data.__dict__)
