# Collections module has already been imported.
class Stack:
    def __init__(self):
        self.storage = []
        self.size = 0

    def push(self, data):
        self.size += 1
        self.storage.push(data)

    def pop(self):
        self.size -= 1
        return self.storage.pop(0)


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def validate_BST_Itr(self, root):
        # Return type should be Boolean
        is_bst = True
        stack = Stack()
        stack.push(root)
        while is_bst is True and stack.size > 0:

        return is_bst
