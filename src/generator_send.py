import math
from typing import Generator, Callable


def wave(amplitude: float, steps: int) -> Generator[float, None, None]:
    """Generate sin wave

    Args:
        amplitude (float): amplitude of sin-wave
        steps (int): steps to generate sin-wave

    Yields:
        Generator[float, None, None]: Next step's sin wave
    """
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output


def wave_modulating(steps: int) -> Generator[float, float, None]:
    """Generate AM radio signal

    Args:
        steps (int): steps to generate signal

    Yields:
        Generator[float, float, None]: Yield next step's output of AM radio signal. Sending is amplitude of the signal.
    """
    step_size = 2 * math.pi / steps
    amplitude = yield  # 最初はNoneでなければいけない
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output


def transmit(output: float) -> None:
    """Stdout sin-wave

    Args:
        output (float): value of sin-wave
    """
    if output is None:
        print(f"Output is None")
    else:
        print(f"Output: {output:>5.1f}")


def output_decorator(func: Callable) -> Callable:
    """wrapper of transmit output

    Args:
        func (Callable): function

    Returns:
        Callable: decorated output of function
    """

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("-" * 10)

    return wrapper


@output_decorator
def run(it: Callable[[float, int], float]) -> None:
    """run sending signal

    Args:
        it (Callable[[float, int], float]): Generator Object of sin-wave generator
    """
    for output in it:
        transmit(output)


def run_modulating(it: Callable[[int], float]):
    amplitudes = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)


def complex_wave() -> Generator[float, None, None]:
    """Generate sin-wave in complex sequence

    Yields:
        Generator[float, None, None]: Next value of sin-wave
    """
    yield from wave(7.0, 3)
    yield from wave(2.0, 4)
    yield from wave(10.0, 5)


def complex_wave_modulating() -> Generator[float, None, None]:
    """Bad example. Generate AM radio signal in complex sequence

    Yields:
        Generator[float, None, None]: Next value of AM radio signal
    """
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)


if __name__ == "__main__":
    # ラジオから信号を送出する
    run(wave(3.0, 8))

    # AMラジオ信号のように, 入力に基づいて振幅が変化する信号を送出する
    run_modulating(wave_modulating(12))

    # 複数のsin波から構成される信号を送出する
    run(complex_wave())

    # 複数のAMラジオ信号から構成される信号を送出する
    # 出力に多数のNoneが含まれてしまう
    # このような場合はsendメソッドを使わず, wave_modulatingにamplitude_it, stepsを渡して,
    # amplitudeは外で管理するほうがよい
    run_modulating(complex_wave_modulating())
