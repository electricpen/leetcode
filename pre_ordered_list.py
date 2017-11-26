pre_ordered_list = []


class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def preorder(self, root):
        left = root.get_left_child()
        right = root.get_right_child()
        pre_ordered_list.append(root.data)
        if left != None:
            self.preorder(left)
        if right != None:
            self.preorder(right)
        return

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data


print(pre_ordered_list)

test_tree = BinaryTree(1)
left1 = BinaryTree(2)
right1 = BinaryTree(3)
test_tree.right_child = right1
test_tree.left_child = left1
print(test_tree.get_root_val())
print(test_tree.get_left_child().get_root_val())
print(test_tree.get_right_child())
left2 = BinaryTree(4)
left1.left_child = left2
right2 = BinaryTree(5)
left1.right_child = right2
left3 = BinaryTree(6)
right1.left_child = left3
right3 = BinaryTree(7)
right1.right_child = right3
print(test_tree.get_left_child().get_root_val())

test_tree.preorder(test_tree)
print(pre_ordered_list)
