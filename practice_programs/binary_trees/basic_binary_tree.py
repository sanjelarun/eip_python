class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


def inorder_tree_travesal(root : BinaryTreeNode):
    if root:
        inorder_tree_travesal(root.left)
        print(root.data)
        inorder_tree_travesal(root.right)

def preorder_tree_travesal(root : BinaryTreeNode):
    if root:
        print(root.data)
        preorder_tree_travesal(root.left)
        preorder_tree_travesal(root.right)
def post_order_tree_travesal(root: BinaryTreeNode):
    if root:
        post_order_tree_travesal(root.left)
        post_order_tree_travesal(root.right)
        print(root.data)
left_node_leaf = BinaryTreeNode(4)
right_child_leaf = BinaryTreeNode(5)
left_child = BinaryTreeNode(2, left_node_leaf,right_child_leaf)
rigt_child = BinaryTreeNode(3)
root_node =BinaryTreeNode(1,left_child, rigt_child)
print("In-order")
inorder_tree_travesal(root_node)
print("Pre-order")
preorder_tree_travesal(root_node)
print("Post order")
post_order_tree_travesal(root_node)