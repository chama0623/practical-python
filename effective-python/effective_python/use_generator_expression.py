if __name__ == "__main__":
    # ファイルの1行ごとの文字数を取得する
    # 大きな内包表記は入力が大量だと, 膨大な量のメモリを消費する
    data_path = "effective_python/dataset/my_file.txt"
    value = [len(x) for x in open(data_path)]
    print(value)

    # ジェネレータ式による改善
    it = (len(x) for x in open(data_path))  # ジェネレータオブジェクト
    value = [i for i in it]
    print(value)

    # ジェネレータの組み合わせ
    it = (len(x) for x in open(data_path))
    roots = ((x, x**2) for x in it)
    print(next(roots))
