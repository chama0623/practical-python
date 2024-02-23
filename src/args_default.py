from datetime import datetime
from time import sleep


def log(message: str, when: datetime = datetime.now()) -> None:
    """ロギングメッセージとその時間を表示する

    Args:
        message (str): ロギングメッセージ
        when (datetime, optional): 時間. Defaults to datetime.now().
    """
    print(f"{when}: {message}")


def log2(message: str, when: str | None = None) -> None:
    """ロギングメッセージとその時間を表示する関数の改善例.

    Args:
        message (str): ロギングメッセージ
        when (str | None, optional): 時間. Defaults to None.
    """
    if when is None:
        when = datetime.now()
    print(f"{when}: {message}")


if __name__ == "__main__":
    # デフォルト引数は定義時に1回しか評価されないため, 期待通りの動作にならない
    log("Hi there!")  # 2024-02-15 10:32:25.099506: Hi there!
    sleep(0.1)
    log("Hi again!")  # 2024-02-15 10:32:25.099506: Hi again!

    # 改善例
    log2("Hi there!")
    sleep(0.1)
    log2("Hi again!")
