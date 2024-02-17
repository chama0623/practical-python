if __name__ == "__main__":
    # リストの各要素の2乗を求めるリスト内包表記
    # map, filterよりも内包表記を使ったほうが良い例
    a = list(range(1, 11))
    squares = [x**2 for x in a]
    print(squares)

    # 2で割り切れる2乗値のみをフィルタリングする内包表記
    even_squares = [x**2 for x in a if x % 2 == 0]
    print(even_squares)

    # 辞書内包表記, 集合内包表記
    even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
    even_squares_set = {x**2 for x in a if x % 2 == 0}
    print(even_squares_dict)
    print(even_squares_set)
