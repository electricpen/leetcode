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
            if root.left_child is not None:
                self.insert(root.left_child, data)
            else:
                new_node = TreeNode(data)
                root.left_child = new_node
        elif data > root.data:
            if root.right_child is not None:
                self.insert(root.right_child, data)
            else:
                new_node = TreeNode(data)
                root.right_child = new_node


root = TreeNode(10)
tree = BinaryTree(root)
tree.insert(root, 5)
tree.insert(root, 3)
tree.insert(root, 4)
tree.insert(root, 15)
tree.insert(root, 12)
print(tree)
