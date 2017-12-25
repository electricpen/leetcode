# Collections module has already been imported.
class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class Stack:
    def __init__(self):
        self.storage = []
        self.size = 0

    def push(self, data):
        self.size += 1
        self.storage.append(data)

    def pop(self):
        self.size -= 1
        return self.storage.pop()


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def validate_BST_Itr(self, root):
        # Return type should be Boolean
        stack = Stack()
        stack.push(root)
        grandparent = root
        while stack.size > 0:
            current = stack.pop()
            if current.right_child is not None:
                if current.right_child.data > current.data and current.right_child.data > grandparent.data:
                    stack.push(current.right_child)
                else:
                    return False
            if current.left_child is not None:
                if current.left_child.data < current.data and current.left_child < grandparent.data:
                    stack.push(current.left_child)
                else:
                    return False
            grandparent = current
        return True


test_root = TreeNode(10)
test_root.left_child = TreeNode(5)
test_root.right_child = TreeNode(15)
test_bst = BinaryTree(test_root)
test_bst.validate_BST_Itr(test_root)
