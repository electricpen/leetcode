class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return '%s' % self.data


class BinaryTree:

    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    def insert(self, root, data):
        # Return the new root
        if data < root.data:
            if root.left_child is None:
                root.left_child = TreeNode(data)
                return self.root
            else:
                return root.insert(root.left_child, data)
        elif data > root.data
            if root.right_child is None:
                root.right_child = TreeNode(data)
                return self.root
            else:
                return self.insert(root.right_child, data)


root = TreeNode(4)
tree = BinaryTree(root)
tree.insert(root, 2)
tree.insert(root, 8)
tree.insert(root, 5)
tree.insert(root, 10)
tree.insert(root, 6)
