import timeit
from typing import Generator

ITER_COUNT = 1_000_000


def child() -> Generator[int, None, None]:
    """Generate numbers from 0 to ITER_COUNT

    Yields:
        Generator[int, None, None]: The next number in the sequence from 0 to ITER_COUNT
    """
    for i in range(ITER_COUNT):
        yield i


def slow() -> Generator[int, None, None]:
    """Generate numbers from 0 to ITER_COUNT using yield

    Yields:
        Generator[int, None, None]: The next number in the sequence from 0 to ITER_COUNT
    """
    for i in child():
        yield i


def fast() -> Generator[int, None, None]:
    """Generate numbers from 0 to ITER_COUNT using yield from

    Yields:
        Generator[int, None, None]: The next number in the sequence from 0 to ITER_COUNT
    """
    yield from child()


if __name__ == "__main__":
    baseline = timeit.timeit(stmt="for _ in slow(): pass", globals=globals(), number=50)
    print(f"Manual nesting {baseline:.2f}s")

    comparison = timeit.timeit(
        stmt="for _ in fast(): pass", globals=globals(), number=50
    )
    print(f"Comparison nesting {comparison:.2f}s")

    reduction = -(comparison - baseline) / baseline
    print(f"{reduction:.1%} less time")

    # Manual nesting 8.29s
    # Comparison nesting 6.93s
    # 16.4% less time
