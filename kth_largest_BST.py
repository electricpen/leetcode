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

    def list_nodes(self):
        ordered_list = []

        def traverse(root):
            if root = None:
                return
            else:
                traverse(root.left_child)
                ordered_list.append(root)
                traverse(root.right_child)
        traverse(self.root)
        return ordered_list

    def find_kth_largest(self, root, k):
            # Return Element should be of type TreeNode
        if not root:
            return None
        list = self.list_nodes()
        return list[-k]
