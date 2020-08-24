class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


def sum_root_to_leaf(tree: BinaryTreeNode, partial_path = 0):
    if not tree:
        return 0

    partial_path = partial_path * 2 + tree.data

    if not tree.left and not tree.right:
        return partial_path

    return sum_root_to_leaf(tree.left,partial_path) + sum_root_to_leaf(tree.right, partial_path)


C = BinaryTreeNode(0)
D = BinaryTreeNode(1)
B = BinaryTreeNode(0, C, D)
F = BinaryTreeNode(1)
E = BinaryTreeNode(1,None, F)
A = BinaryTreeNode(1, B, E)

print(sum_root_to_leaf(A))