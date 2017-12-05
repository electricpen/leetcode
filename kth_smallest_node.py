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

    def insert(self, root, val):
        if val < root.data:
            if root.left_child is None:
                root.left_child = TreeNode(val)
            else:
                self.insert(root.left_child, val)
        elif val > root.data:
            if root.right_child is None:
                root.right_child = TreeNode(val)
            else:
                self.insert(root.right_child, val)

    def find_kth_smallest(self, root, k):
        # Return element should be of Type TreeNode
        list = []

        def traverse(root):
            if root.size(root) == 1:
                list.append(root.data)
            elif root.size > 1:
                if root.left_child:
                    traverse(root.left_child)
                list.append(root.data)
                if root.right_child:
                    traverse(root.right_child)
        traverse(root)
