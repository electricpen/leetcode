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
        self.head = Node()
        self.head.setData(head)

    def show(self):
        pointer = self.head
        while pointer != None:
            print(pointer.getData())
            pointer = pointer.next

    def insert(self, data):
        pointer = self.head
        new_node = Node()
        new_node.setData(data)
        if self.head is None:
            self.setHead(data)
        else:
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = new_node

    def reverse(self):
        last = None
        current = self.head
        while current != None:
            next = current.next
            current.next = last
            last = current
            current = next
        self.head = last


test = SinglyLinkedList()
print('Should be empty:')
test.show()
test.insert(1)
print('Should be 1')
test.show()
test.insert(2)
print('Should be 1, 2.')
test.show()
test.reverse()
print('Should be 2, 1')
test.show()
