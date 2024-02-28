from collections.abc import Sequence


class FrequencyList(list):

    def __init__(self, members):
        """
        Initialize a FrequencyList instance.

        Args:
            members (Iterable): An iterable containing the initial elements of
            the FrequencyList.
        """
        super().__init__(members)

    def frequency(self):
        """
        Calculate the frequency of each element in the FrequencyList.

        Returns:
            dict: A dictionary where keys are elements of the FrequencyList
            and values are their respective frequencies.
        """
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts


# シーケンスのセマンティクスを提供する二分木を実装する
# BinaryNodeはlistのサブクラスではない
class BinaryNode:
    """Binary Node Class"""

    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class IndexableNode(BinaryNode):
    def _traverse(self):
        if self.left is not None:
            yield from self.left._traverse()
        yield self
        if self.right is not None:
            yield from self.right._traverse()

    def __getitem__(self, index: int):
        for i, item in enumerate(self._traverse()):
            if i == index:
                return item.value
        raise IndexError(f"Index {index} is out of range")


class SequenceNode(IndexableNode):
    def __len__(self):
        for count, _ in enumerate(self._traverse(), 1):
            pass
        return count


class BadType(Sequence):
    pass


class BetterType(SequenceNode, Sequence):
    pass


if __name__ == "__main__":
    # listを継承しているのでlistが提供する標準機能はすべて使える
    foo = FrequencyList(["a", "b", "a", "c", "b", "a", "d"])
    print(f"Length is {len(foo)}")
    foo.pop()
    print(f"After Pop : {foo}")
    print(f"Frequency : {foo.frequency()}")

    tree = SequenceNode(
        10,
        left=IndexableNode(
            5, left=IndexableNode(2), right=IndexableNode(6, right=IndexableNode(7))
        ),
        right=IndexableNode(15, left=IndexableNode(11)),
    )

    # __getitem__(), __len__()の他にもcount, indexを実装する必要があり, シーケンスとして扱えるようにするのは大変
    print("LRR is", tree.left.right.right.value)
    print("Index 0 is", tree[0])
    print("Index 1 is", tree[1])
    print("Tree length is", len(tree))

    # collencionts.abcを使って抽象基底クラスに最低限必要なメソッド以外を自動提供できるようにする
    # 最低限必要なメソッドがないとエラーになるよ
    # bar = BadType()
    # Traceback (most recent call last):
    #   File "/workspace/src/collections_abc.py", line 90, in <module>
    #     bar = BadType()
    #           ^^^^^^^^^
    # TypeError: Can't instantiate abstract class BadType without an
    # implementation for abstract methods '__getitem__', '__len__'

    tree = BetterType(
        10,
        left=IndexableNode(
            5, left=IndexableNode(2), right=IndexableNode(6, right=IndexableNode(7))
        ),
        right=IndexableNode(15, left=IndexableNode(11)),
    )
    print("Index of 7 is", tree.index(7))
    print("Count of 10 is", tree.count(10))
