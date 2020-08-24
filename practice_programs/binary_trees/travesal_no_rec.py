class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def in_order_no_rec(tree):
    s, result = [],[]
    while s or tree:
        if tree:
            s.append(tree)
            tree = tree.left
        else:
            tree = s.pop()
            result.append(tree.data)
            tree = tree.right
    return result


def preorder_no_rec(tree):
    path, result  =[tree],[]
    while path:
        curr = path.pop()
        if curr:
            result.append(curr.data)
            path += [curr.right, curr.left]
    return result


def post_order_no_rec(tree):
    path, result = []
left_node_leaf = BinaryTreeNode(4)
right_child_leaf = BinaryTreeNode(5)
left_child = BinaryTreeNode(2, left_node_leaf,right_child_leaf)
rigt_child = BinaryTreeNode(3)
root_node =BinaryTreeNode(1,left_child, rigt_child)
print("In-order")
print(in_order_no_rec(root_node))
print("Pre-order")
print(preorder_no_rec(root_node))