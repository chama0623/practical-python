import itertools

if __name__ == "__main__":
    # 名前の文字数が最も長い人の名前を表示する
    names = ["Cecilia", "Lise", "Marie"]
    counts = [len(n) for n in names]

    longest_name = None
    max_count = 0
    # name, countの長さが異なる場合は, 最小のリストの長さ回反復
    for name, count in zip(names, counts):
        if count > max_count:
            longest_name = name
            max_count = count
    print(f"{longest_name=}")

    # itertools.zip_longestを使うと最大のリストの長さ回反復
    names.append("Rosalind")
    for name, count in itertools.zip_longest(names, counts):
        print(f"{name}: {count}")
