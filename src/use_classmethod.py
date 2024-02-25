import os
import random
from threading import Thread
from typing import Generator, Iterable, Optional


class InputData:
    """Common class of input data"""

    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    """Concrete class of InputData"""

    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path

    def read(self) -> str:
        """read self.path's file

        Returns:
            str: content of file
        """
        with open(self.path) as f:
            return f.read()


class Worker:
    """Worker of processing input data"""

    def __init__(self, input_data: InputData) -> None:
        self.input_data = input_data
        self.result = None

    def map(self) -> None:
        raise NotImplementedError

    def reduce(self, other: "Worker") -> None:
        raise NotImplementedError


class LineCountWorker(Worker):
    """Concrete class of Worker"""

    def map(self) -> None:
        """Count the number of lines in a file"""
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self, other: "LineCountWorker") -> None:  # type: ignore[override]
        """Aggregate the number of lines in file

        Args:
            other (LineCountWorker): LineCountWorker object to be aggregated
        """
        if self.result is not None and other.result is not None:
            self.result += other.result


def generate_inputs(data_dir: str) -> Generator[PathInputData, None, None]:
    """Get file path from args dir

    Args:
        data_dir (str): dir path

    Yields:
        Generator[PathInputData, None, None]: PathInputData object of each file content
    """
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list: Iterable[InputData]) -> list[LineCountWorker]:
    """Create list of workers

    Args:
        input_list (Iterable[InputData]): iterable object of InputData instance

    Returns:
        list[LineCountWorker]: list of LineCountWorker instance
    """
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


def execute(workers: list[LineCountWorker]) -> Optional[int]:
    """Execute MapReduce model

    Args:
        workers (list[LineCountWorker]): Workers to execute

    Returns:
        Optional[int]: Total count of lines in files
    """
    # Map step
    # workersリストの各LineCountWorkerオブジェクトをマッピングする
    threads = [Thread(target=w.map) for w in workers]
    # 各ファイルの行数を並列に数える
    for thread in threads:
        thread.start()  # 処理開始
    for thread in threads:
        thread.join()  # 処理終了を待つ

    # Reduce step
    # 1番目のLineCountWorker.reduce()で集計を行う
    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(data_dir: str) -> Optional[int]:
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


def write_test_files(tmpdir: str) -> None:
    """Generate sample file for test MapReduce

    Args:
        tmpdir (str): dir path
    """
    os.makedirs(tmpdir, exist_ok=True)
    for i in range(100):
        with open(os.path.join(tmpdir, str(i)), "w") as f:
            f.write("\n" * random.randint(0, 100))


if __name__ == "__main__":
    # MapReduce : 大規模データセットを分散処理するためのプログラミングモデルおよび処理フレームワーク
    # MapReduceはMapステップ, Reduceステップの2つのステップから構成される.
    # Mapステップ : 入力データをキーと値のペアでマッピングし, 部分的なタスクに分割して並列処理を行う.
    # Reduceステップ : Mapステップの処理結果を集計して最終的な出力を得る.
    tmpdir = "test_inputs"
    write_test_files(tmpdir)
    result = mapreduce(tmpdir)
    print(f"There are {result} lines")
