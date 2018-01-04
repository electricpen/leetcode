class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def insert(self, node, root):
        if self is None:
            self = node
        else:
            if root.data > node.data:
                if root.left_child is None:
                    root.left_child = node
                else:
                    self.insert(node, root.left_child)
            elif root.data < node.data:
                if root.right_child is None:
                    root.right_child = node
                else:
                    self.insert(node, root.right_child)

    def create(self, data):
        for item in data:
            new_node = BinaryTree(item)
            self.insert(new_node, self)

    def inorder_iterative(self):
        inorder_list = []
        stack = []
        if self is not None:
            curr = self
            stack.append(self)
        while len(stack) > 0:
            if curr:
                while curr.left_child:
                    stack.append(curr.left_child)
                    curr = curr.left_child
            curr = stack.pop()
            inorder_list.append(curr.data)
            if curr.right_child:
                stack.append(curr.right_child)
                curr = curr.right_child
            else:
                curr = None
        return inorder_list

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data


test = BinaryTree(10)
test.create([5, 3, 7, 6, 8, 15, 20])
print(test.inorder_iterative())
