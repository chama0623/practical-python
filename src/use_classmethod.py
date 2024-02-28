import os
import random
from threading import Thread
from typing import Generator, Iterable, Optional


class GenericInputData:
    """Generic class of InputData"""

    def read(self) -> str:
        """Read the inpu data.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config: dict[str, str]) -> Iterable["GenericInputData"]:
        """Generate input data instances based on the given configuration.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError


class PathInputData(GenericInputData):
    """Concrete class of InputData"""

    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path

    def read(self) -> str:
        """Read the content of the file specified by self.path.

        Returns:
            str: content of the file.
        """
        with open(self.path) as f:
            return f.read()

    @classmethod
    def generate_inputs(cls, config: dict[str, str]) -> Iterable["PathInputData"]:
        """Generate PathInputData instances based on the given configuration.

        Yields:
            Iterable[PathInputData]: Instances of PathInputData.
        """
        data_dir = config["data_dir"]
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker:
    """Worker of processing input data"""

    def __init__(self, input_data: GenericInputData) -> None:
        self.input_data = input_data
        self.result = 0

    def map(self) -> None:
        """Perform the mapping step of processing.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError

    def reduce(self, other: "GenericWorker") -> None:
        """Perform the reduction step of processing.

        Args:
            other (GenericWorker): Another worker instance to be reduced with.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError

    @classmethod
    def create_workers(
        cls, input_class: type[GenericInputData], config: dict[str, str]
    ) -> list["GenericWorker"]:
        """Create a list of workers based on the provided input class and
        configuration.

        Args:
            input_class (GenericInputData): The input data class to be used
            for generating inputs.
            config (Dict[str, str]): Configuration containing data directory
            path.

        Returns:
            List[GenericWorker]: A list of worker instances.

        Raises:
            NotImplementedError: If the input class does not support
            generate_inputs method.
        """
        workers = []
        # cls()で新しいGenericWorkerインスタンスを作る
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
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
        Generator[PathInputData, None, None]: PathInputData object of each
        file content
    """
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list: Iterable[GenericInputData]) -> list[LineCountWorker]:
    """Create list of workers

    Args:
        input_list (Iterable[GenericInputData]): iterable object of
        GenericInputData instance

    Returns:
        list[LineCountWorker]: list of LineCountWorker instance
    """
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


def execute(workers: list[GenericWorker]) -> Optional[int]:
    """Execute MapReduce model

    Args:
        workers (list[GenericWorker]): Workers to execute

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


def mapreduce(
    worker_class: type[GenericWorker],
    input_class: type[GenericInputData],
    config: dict[str, str],
) -> Optional[int]:
    """Execute the MapReduce process using the provided worker class, input
    class, and configuration.

    Args:
        worker_class (type[GenericWorker]): The worker class responsible for
        processing input data.
        input_class (type[GenericInputData]): The input data class to be used for
        generating inputs.
        config (dict[str, str]): Configuration containing data directory path.

    Returns:
        Optional[int]: The total count of lines in the files processed by the
        MapReduce process, or None if the process fails.

    Raises:
        NotImplementedError: If the worker class or input class does not
        support the required methods.
    """
    workers = worker_class.create_workers(input_class, config)
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

    config = {"data_dir": tmpdir}
    result = mapreduce(LineCountWorker, PathInputData, config)
    print(f"There are {result} lines")
