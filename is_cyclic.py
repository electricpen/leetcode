class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def insert(self, node):
        if self.head is None:
            self.setHead(node)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def create(self, data):
        for item in data:
            new_node = Node()
            new_node.setData(item)
            self.insert(new_node)

    def is_cyclic(self):
        if self.head is None:
            return False
        else:
            fast = self.head.next
            slow = self.head
            while fast is not None and fast.data != slow.data:
                slow = slow.next
                fast = fast.next
                if fast is not None and fast.data != slow.data:
                    fast = fast.next
        return fast.data == slow.data
