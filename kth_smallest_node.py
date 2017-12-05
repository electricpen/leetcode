class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return '%s' % self.data

    def size(self, root):
        if root == None:
            return 0
        else:
            return (self.size(root.left_child) + 1 + self.size(root.right_child))


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
        if self.root is None:
            self.root = TreeNode(val)
        elif val < root.data:
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
        # Helper function
        def is_leaf(root):
            return root.left_child == None and root.right_child == None

        list = []
        if self.size(self.root) < k:
            return None

        def traverse(root):
            if is_leaf(root):
                list.append(root.data)
            else:
                if root.left_child:
                    traverse(root.left_child)
                list.append(root.data)
                if root.right_child:
                    traverse(root.right_child)
        traverse(root)
        return list[k - 1]


seed = [10, 5, 3, 1, 7, 15, 14, 17]
test = BinaryTree()
for num in seed:
    test.insert(test.root, num)
print(test.find_kth_smallest(test.root, 2))
