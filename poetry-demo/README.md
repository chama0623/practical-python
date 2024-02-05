# poetry-demo

1. プロジェクトのセットアップ
```
$ poetry new poetry-demo
```
```
poetry-demo
├── pyproject.toml
├── README.md
├── poetry_demo
│   └── __init__.py
└── tests
    └── __init__.py
```

2. パッケージの追加(コマンドラインから追加する場合)
```
$ poetry add パッケージ
```

2. パッケージの追加(pyproject.tomlから追加する場合)
```
[tool.poetry]
name = "poetry-demo"
version = "0.1.0"
description = ""
authors = ["Sébastien Eustace <sebastien@eustace.io>"]
readme = "README.md"
packages = [{include = "poetry_demo"}]

[tool.poetry.dependencies]
python = "^3.7"
### ここに記述する ###

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
```
$ poetry install
```

3. 仮想環境の有効化
```
$ poetry config virtualenvs.create true
```