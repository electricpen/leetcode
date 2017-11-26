post_ordered_list = []


class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def postorder(self, node):
        if node != None:
            node = self
        if node.left_child != None:
            self.postorder(node.left_child)
        elif node.right_child != None:
            self.postorder(node.right_child)
        post_ordered_list.append(node.get_root_val)
        return

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data
