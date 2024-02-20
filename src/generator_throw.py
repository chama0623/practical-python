from typing import Generator


class MyError(Exception):
    pass


def my_generator() -> Generator[int, None, None]:
    yield 1
    yield 2
    yield 3


def my_generator2() -> Generator[int, None, None]:
    yield 1
    try:
        yield 2
    except MyError:
        print("Got MyError!")
    else:
        yield 3
    yield 4


if __name__ == "__main__":
    # Generator Object.throwはyield式が出力を受け取った直後に例外を送出する
    it1 = my_generator()
    print(next(it1))
    print(next(it1))
    # print(it1.throw(MyError("test error")))

    # 例外を補足する例
    # Mmy_generator2()は読みにくい - throwを使った状態遷移は避ける
    it2 = my_generator2()
    print(next(it2))
    print(next(it2))
    print(it2.throw(MyError("test error")))
