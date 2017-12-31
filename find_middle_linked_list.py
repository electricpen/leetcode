import math


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

    def size(self):
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def initialize(self, data):
        for item in data:
            new_node = Node()
            new_node.setData(item)
            if self.head == None:
                self.head = new_node
                curr = self.head
            else:
                curr.next = new_node
                curr = curr.next

    def find_middle_node(self):
        if self.head is None:
            return None
        mid = int(math.ceil(self.size() / 2))
        curr = self.head
        for index in range(1, mid):
            curr = curr.next
        return curr.getData()


test = SinglyLinkedList()
test.initialize([1, 2, 3, 4, 5])
print(test.size())
print(test.find_middle_node())

"""
Optimal solution is to use two pointers and loop through with one pointer moving
twice every iteration. You return the slow pointer since it should be at the
halfway point.
"""
