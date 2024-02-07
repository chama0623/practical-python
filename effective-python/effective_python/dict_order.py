def my_func(**kwargs):
    """キーワード引数を出力する"""
    for key, value in kwargs.items():
        print(f"{key} = {value}")


if __name__ == "__main__":
    # ペットの種類と名前
    # dictの出力は挿入順になる
    baby_names = {"cat": "kitten", "dog": "puppy"}
    print(baby_names)  # {'cat': 'kitten', 'dog': 'puppy'}

    # キーワード引数も入力順を保持する
    my_func(goose="gosling", kangaroo="joey")
