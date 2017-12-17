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

    def find_min(self, root):
        # Return element should be of type TreeNode
        if root.left_child is None and root.righright_childt is None:
            return root.data
        else:
            if root.left_child:
                return self.find_min(root.left_child)
            elif root.right_child:
                return self.find_min(root.right_child)
