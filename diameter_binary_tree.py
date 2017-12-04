class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

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

    def is_leaf(self, node):
        return node.left_child is None and node.right_child is None

    def max_length(self, root):
        current = {'length': 0}
        result = {'num': 0}

        def traverse(root):
            if self.is_leaf(root):
                if current['length'] + 1 > result['num']:
                    result['num'] = current['length'] + 1
            else:
                current['length'] += 1
                if root.left_child is not None:
                    traverse(root.left_child)
                if root.right_child is not None:
                    traverse(root.right_child)
                current['length'] -= 1

        if root is not None:
            traverse(root)
        return result['num']

    def diameter(self, root):
        if root is None:
            return 0
        elif self.is_leaf(root):
            return 1
        else:
            return self.max_length(root.left_child) + self.max_length(root.right_child) + 1


# Testing area
list = [5, 8, 1, 7, 6, 15, 13, 20, 25]
node = TreeNode(10)
test_tree = BinaryTree(node)
for val in list:
    test_tree.insert(test_tree.root, val)
print(test_tree.diameter(test_tree.root))
