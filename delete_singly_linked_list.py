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
                else:
                    self.head = None
            else:
                prev = current
                current = current.next
