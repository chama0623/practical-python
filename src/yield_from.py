from typing import Generator, Callable

# type.Generator: Generator[YieldType, SendType, ReturnType]
# YieldType : yieldする値の型
# SendType : generator_object.send(value)でgenerator_objectに送る値の型
# ReturnType : StopIteration例外時に返す値の型
def move(period:int, speed:float)->Generator[float, None, None]:
    """指定されたフレームのあいだ, イメージの移動速度を返す

    Args:
        period (int): 移動するフレーム数
        speed (float): 移動速度

    Yields:
        Generator[float, None, None]: 移動速度を返す. YieldType, ReturnTypeはNone
    """
    for _ in range(period):
        yield speed
        
def pause(delay:int)-> Generator[int, None, None]:
    """指定されたフレームのあいだ, イメージを停止させる

    Args:
        delay (int): 停止するフレーム数

    Yields:
        Generator[int, None, None]: 移動速度(0)を返す. YieldType, ReturnTypeはNone
    """
    for _ in range(delay):
        yield 0
        
def animate()->Generator[float, None, None]:
    """悪い例. 少しの間高速で移動し, 停止した後, ゆっくりと移動する
    移動と停止を何度も繰り返す場合は読みにくい

    Yields:
        Generator[float, None, None]: 各フレームの移動速度を返す
    """
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta

def animate_composed()->Generator[float, None, None]:
    """yield fromによる改善例. 少しの間高速で移動し, 停止した後, ゆっくりと移動する

    Yields:
        Generator[float, None, None]: 各フレームの移動速度を返す
    """
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)
        
def render(delta:float):
    """アニメーションを描画する. ここでは標準出力に移動速度を表示する.

    Args:
        delta (float): _description_
    """
    print(f"Delta: {delta:.1f}")

def run(func:Callable[[], float])->None:
    """アニメーションを実行する

    Args:
        func (Callable[[], float]): 実行するアニメーションの関数
    """
    for delta in func():
        render(delta)

if __name__ == "__main__":
    run(animate)
    print("-"*10)
    run(animate_composed)