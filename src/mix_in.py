# mix-inクラス
# サブクラスが提供すべき一連の追加メソッドを定義するだけのクラス
# この例では階層構造をdictで表現する関数だけろToDictMixinで定義しておき,
# BinaryTreeがそれを継承している.


class ToDictMixin:
    """Mix-in class to convert to dictionary"""

    def to_dict(self):
        """Convert the in-memory representation of an object into a dictionary
        that can be serialized"""
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        """Recursively traverse a dictionary."""
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        """Recursively traverse a value to handle nested objects."""
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, "__dict__"):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class BinaryTree(ToDictMixin):
    """Binary Tree class with ToDictMixin"""

    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeWithParent(BinaryTree):
    """Binary Tree with Parent class with BinaryTree"""

    def __init__(self, value, left=None, right=None, parent=None) -> None:
        super().__init__(value, left, right)
        self.parent = parent

    def _traverse(self, key, value):
        """Recursively traverse a value to handle nested objects.
        But this method prevents infinite cycle by refering to parent.

        Args:
            key (_type_): _description_
            value (_type_): _description_

        Returns:
            _type_: _description_
        """
        if isinstance(value, BinaryTreeWithParent) and key == "parent":
            return value.value  # prevent cycle
        else:
            return super()._traverse(key, value)


if __name__ == "__main__":
    # BinaryTree
    tree = BinaryTree(
        10,
        left=BinaryTree(7, right=BinaryTree(9)),
        right=BinaryTree(13, left=BinaryTree(1)),
    )
    print(tree.to_dict())

    # BinaryTreeWithParent
    # BinaryTreewithParent._traverseのオーバーライドがない場合は親を参照するので無限ループになる
    root = BinaryTreeWithParent(10)
    root.left = BinaryTreeWithParent(7, parent=root)
    root.left.right = BinaryTreeWithParent(9, parent=root.left)
    print(root.to_dict())
