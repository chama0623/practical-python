if __name__ == "__main__":
    # ディーラーが扱っている車の使用年数から, 1番目, 2番目に古い車とそれ以外の車を取得する
    car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
    car_ages_descending = sorted(car_ages, reverse=True)

    # 悪い例
    oldest = car_ages_descending[0]
    second_oldest = car_ages_descending[1]
    others = car_ages_descending[2:]
    print(oldest, second_oldest, others)

    # catch-all unpackを使った良い例
    oldest, second_oldest, *others = car_ages_descending
    print(oldest, second_oldest, others)

    # 最も古い車, 最も新しい車, それ以外の車を取得する
    oldest, *others, youngest = car_ages_descending
    print(oldest, youngest, others)

    #  1番目, 2番目に新しい車とそれ以外の車を取得する
    *others, second_youngest, youngest = car_ages_descending
    print(youngest, second_youngest, others)
