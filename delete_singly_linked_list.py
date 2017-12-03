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

    # method for deleting a node having a certain data
    def delete(self, data):
        prev = None
        current = self.head
        while current != None:
            if current.data == data:
                if prev != None:
                    prev.next = current.next
                    return
                else:
                    self.head = None
            else:
                prev = current
                current = current.next

    def print(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.next


test = Node()
test.setData(3)
test2 = Node()
test2.setData(5)
test_list = SinglyLinkedList()
test_list.setHead(test)
test_list.head.next = test2
print('before', test_list.print())
test_list.delete(5)
print('after', test_list.print())
