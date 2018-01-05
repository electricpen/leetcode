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
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def construct(self, data):
        for item in data:
            self.insert(item)

    def find_nth_node_from_end(self, n):
        count = 0
        lead = self.head
        trailing = self.head
        while lead is not None:
            lead = lead.next
            if count >= n:
                trailing = trailing.next
            count += 1
        return trailing
