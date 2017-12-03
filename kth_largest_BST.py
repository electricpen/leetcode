class BinaryTree:

    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    # Helper Method
    def size(self, root):
        if root == None:
            return 0
        else:
            return (self.size(root.left_child) + 1 + self.size(root.right_child))

    def depth(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.depth(root.right_child)

    def find_kth_largest(self, root, k):
            # Return Element should be of type TreeNode
        height = depth(self.root)
        if k > height:
            return None
        position = self.root
        for i in range(height - (k - 1)):
            position = position.right_child
        return position.data
