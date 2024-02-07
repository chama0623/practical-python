from collections import defaultdict


class Visits:
    def __init__(self) -> None:
        # 引数でkeyがないときの動作を指定する
        # ここでは新しくsetを作成する
        self.data = defaultdict(set)

    def add(self, country: str, city: str):
        """訪問した国と都市を追加する

        Args:
            country (str): 国名
            city (str): 都市名
        """
        self.data[country].add(city)


if __name__ == "__main__":
    # 訪問した国と都市
    visits = {
        "Mexico": {"Tulum", "Puerto Vallarta"},
        "Japan": {"Hakone"},
    }

    # FranceのArlesを追加する
    # setdefaultを使うとkeyがない場合に追加されるが煩雑
    visits.setdefault("France", set()).add("Arles")
    print(visits)

    # defaultdictを使う
    business_visits = Visits()
    business_visits.add("England", "Bath")
    business_visits.add("England", "London")
    print(business_visits.data)
