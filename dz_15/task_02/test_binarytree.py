from dz_14_tst import *
import pytest


class TestNode:
    @pytest.fixture
    def tree(self):
        root = Node(4)
        root.insert(2)
        root.insert(1)
        root.insert(3)
        root.insert(6)
        root.insert(5)
        root.insert(7)
        return root

    def test_insert(self, tree):
        tree.insert(8)
        assert tree.right.right.right.val == 8

    def test_min_val_node(self, tree):
        assert tree.min_val_node() == 1

    def test_max_val_node(self, tree):
        assert tree.max_val_node() == 7

    def test_delete(self, tree):
        tree.delete(7)
        assert tree.right.val == 6
        assert tree.right.right is None