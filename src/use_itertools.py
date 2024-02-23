import itertools

if __name__ == "__main__":
    # 複数のIteratorを組み合わせて1つのシーケンスにする
    it = itertools.chain([1, 2, 3], [4, 5, 6])
    print(list(it))

    # 1つの値を何回も繰り返す
    it = itertools.repeat("hello", 3)
    print(list(it))

    # Iteratorの要素を繰り返す
    it = itertools.cycle([1, 2])
    result = [next(it) for _ in range(10)]
    print(result)

    # 長さの異なる2つのシーケンスの最大長でzipする
    keys = ["one", "two", "three"]
    values = [1, 2]
    it = itertools.zip_longest(keys, values)
    result = list(it)
    print(result)

    # 複製せずにindexでIteratorをスライスする
    values = list(range(10))
    first_five = itertools.islice(values, 5)  # Iterator Object
    print(f"first five: {list(first_five)}")

    middle_odds = itertools.islice(values, 2, 8, 2)
    print(f"middle odds: {list(middle_odds)}")

    # 述語関数がFalseになるまでIteratorの要素を返す
    less_than_seven = lambda x: x < 7
    it = itertools.takewhile(less_than_seven, values)
    print(list(it))

    # 述語関数がFalseになるまでIteratorの要素をスキップする
    it = itertools.dropwhile(less_than_seven, values)
    print(list(it))

    # 累積を計算する
    sum_reduce = itertools.accumulate(values)
    print(f"Sum : {list(sum_reduce)}")

    # 1つ以上のIteratorの直積を返す
    single = itertools.product([1, 2], repeat=2)
    print(f"Single : {list(single)}")

    multiple = itertools.product([1, 2], ["a", "b"])
    print(f"Multiple : {list(multiple)}")

    # 順列を返す
    # 4P2
    it = itertools.permutations([1, 2, 3, 4], 2)
    print(list(it))

    # 組み合わせ
    # 4C2
    it = itertools.combinations([1, 2, 3, 4], 2)
    print(list(it))

    # 重複を許す組み合わせ
    it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
    print(list(it))
