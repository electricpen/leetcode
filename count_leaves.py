class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def number_of_leaves(self, root):
        if root.left_child is None and root.right_child is None:
            return 1
        else:
            return self.number_of_leaves(root.left_child) + self.number_of_leaves(root.right_child)
