if __name__ == "__main__":
    # 多次元リストを1次元リストに変換する
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [x for row in matrix for x in row]
    print(flat)

    # 各要素を2乗する複雑な内包表記
    matrix = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
    squared = [
        [[x**2 for x in sublist2] for sublist2 in sublist1] for sublist1 in matrix
    ]
    print(squared)

    # 3つ以上の式の場合は通常のループ文の方が分かりやすいので避けるべき
    # 例えば 3重の内包表記, 1つの内包表記に2つの条件, 2つの内包表記に1つの条件
    # このような場合ではジェネレータのヘルパー関数を書くのが良い
    squared = []
    for sublist1 in matrix:
        tmp = []
        for sublist2 in sublist1:
            tmp.append([x**2 for x in sublist2])
        squared.append(tmp)
    print(squared)
