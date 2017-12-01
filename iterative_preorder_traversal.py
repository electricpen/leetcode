class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def preorder_iterative(self):
        pre_ordered_List = []
        stack = []
        stack.append(self)
        while len(stack) > 0:
            current = stack.pop()
            pre_ordered_List.append(current.get_root_val())
            if current.get_right_child():
                stack.append(current.get_right_child())
            if current.get_left_child():
                stack.append(current.get_left_child())

        return pre_ordered_List

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data
