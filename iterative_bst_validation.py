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
        self.storage.push(data)

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
        while is_bst is True and stack.size > 0:
            current = stack.pop()
            if current.right_child is not None:
                if current.right.child.data > current.data:
                    stack.push(current.right_child)
                else:
                    return False
            if current.left_child is not None:
                if current.left_child.data < current.data:
                    stack.push(current.left_child)
                else:
                    return False
        return True
