from datetime import datetime, timedelta
from typing import Type


# 単純な数値属性の計算を@propertyの振る舞いで行う
class Bucket:
    """Leaky bucket class"""

    def __init__(self, period: float) -> None:
        self.period_delta = timedelta(seconds=period)  # 割り当て量の存在する時間
        self.reset_time = datetime.now()
        self.quota = 0  # 割り当て量

    def __repr__(self) -> str:
        return f"Bucket(quota={self.quota})"


def fill(bucket: Bucket, amount: float):
    """Add water to the bucket.

    Args:
        bucket (Bucket): Bucket object to add water
        amount (float): amount of water
    """
    now = datetime.now()
    # 割り当て量の存在する時間が過ぎているとき
    if now - bucket.reset_time > bucket.period_delta:
        # バケツをリセットする
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount


def deduct(bucket: Bucket, amount: float) -> bool:
    """Fetch water from bucket.

    Args:
        bucket (Bucket): Bucket object to fetch water
        amount (float): amount of water

    Returns:
        bool: True when getting water out of the bucket.
    """
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        return False  # このピリオドではバケツに水がない
    if bucket.quota - amount < 0:
        return False  # バケツに水はあるが不十分
    bucket.quota -= amount
    return True  # 水が十分あり, 割り当てを消費した


class NewBucket:
    def __init__(self, period: float) -> None:
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0  # 消費可能なquotaの最大量
        self.quota_consumed = 0  # 消費されたquotaの量

    def __repr__(self):
        return f"NewBucket(max_quota={self.max_quota},quota_consumed={self.quota_consumed})"

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed  # 消費可能な水量

    @quota.setter
    def quota(self, amount: float):
        delta = self.max_quota - amount
        if amount == 0:
            # 割り当て量をリセットする
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # 追加される水量が消費可能な最大水量を超えるとき
            self.max_quota = amount + self.quota_consumed
        else:
            # 消費した水量を更新する
            self.quota_consumed = delta


def control_water(bucket_cls: Type):
    """水をバケツに注いだり, 汲み取ったりする処理

    Args:
        bucket_cls (Type): Class of Bucket or NewBucket
    """
    bucket = bucket_cls(60)
    fill(bucket, 100)  # 100Lまで入れる
    print(bucket)  # 100L

    # 99L消費する
    if deduct(bucket, 99):
        print("Had 99 quota")
    else:
        print("Not enough for 99 quota")

    print(bucket)  # 1L

    # さらに3L消費する
    # バケツに水がないのか, 水はあるが不十分なのか分からない
    if deduct(bucket, 3):
        print("Had 3 quota")
    else:
        print("Not enough for 3 quota")

    print(bucket)  # 1L


if __name__ == "__main__":
    control_water(Bucket)
    print("-" * 10)

    # @propertyによる改善
    control_water(NewBucket)
