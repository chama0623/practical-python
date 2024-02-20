if __name__ == "__main__":
    key = "my_var"
    value = 1.234
    print(f"{key} = {value}")

    # !r : repr関数により表現文字列を取得する
    # < : 左寄せ
    # 10 : 10文字の幅を確保する
    formatted = f"{key!r:<10} = {value:.2f}"
    print(formatted)

    # , : 3桁ごとのカンマ区切り
    # ^ : センタリング
    a = 1234.567
    b = "my string"
    print(f"{a:,.2f}")
    print(f"{b:^20s}")

    # 変数の出力
    detect_accuracy = 0.975
    print(f"{detect_accuracy=}")
