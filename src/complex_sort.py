class Tool:
    def __init__(self, name: str, weight: float) -> None:
        """コンストラクタ

        Args:
            name (str): 工具の名前
            weight (float): 工具の重さ
        """
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name}, {self.weight})"


if __name__ == "__main__":
    tools = [
        Tool("level", 3.5),
        Tool("Hammer", 1.25),  # Hは大文字
        Tool("screwdriver", 0.5),
        Tool("chisel", 0.25),
    ]
    print(f"Unsorted: {tools}")

    # クラスに自然な順序がない場合はソートできない
    # tools.sort() -> TypeError: '<' not supported between instances of 'Tool' and 'Tool'

    # nameでソート
    # 大文字・小文字を区別する場合は大文字, 小文字の順になる
    tools.sort(key=lambda x: x.name.lower())  # 小文字に統一
    print(f"By name: {tools}")

    # weightでソート
    tools.sort(key=lambda x: x.weight)
    print(f"By weight: {tools}\n")

    # weight, 次にnameでソート
    # この方法では, 各要素に降順, 昇順を指定できない
    power_tools = [
        Tool("drill", 4),
        Tool("circular saw", 5),
        Tool("jackhammer", 40),
        Tool("sander", 4),
    ]
    print(f"Unsorted: {power_tools}")

    power_tools.sort(key=lambda x: (x.weight, x.name))
    print(f"By weight, name: {power_tools}")

    # weightの降順, 次にnameの昇順でソートする
    # sortは安定ソートなので, keyが等しいときは入力順を保持する
    power_tools.sort(key=lambda x: x.name)  # name昇順
    power_tools.sort(key=lambda x: x.weight, reverse=True)  # weight降順
    print(f"By weight(desc), name(asc): {power_tools}")
