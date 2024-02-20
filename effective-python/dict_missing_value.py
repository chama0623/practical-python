if __name__ == "__main__":
    # 好きなパンの種類と投票数
    counters = {
        "pumpernickel": 2,
        "sourdough": 1,
    }
    print(counters)

    # 新しくwheatというパンを追加する
    # get : keyを取得するかdefault値を返す
    key = "wheat"
    count = counters.get(key, 0)
    counters[key] = count + 1
    print(counters)

    # 投票数だけでなく, 誰が投票したのかを保持するdict
    votes = {
        "baguette": ["Bob", "Alice"],
        "ciabatta": ["Coco", "Deb"],
    }
    print(votes)

    # パンbriocheにElmerが投票した
    key = "brioche"
    who = "Elmer"
    if (names := votes.get(key)) is None:  # briocheのリストがNone
        votes[key] = names = []  # votes[key], namesに空リストを割り当て
    names.append(who)  # Elmerを追加
