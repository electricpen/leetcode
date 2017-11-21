class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    # method for inserting a new node at the end of a Linked List
    def insertAtEnd(self, data):
        current = self.head
        n = Node()
        n.setData(data)
        while current.next != None:
            current = current.next
        current.next = n
