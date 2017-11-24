class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def insert(self, data):
        pointer = self.head
        if self.head == None:
            self.setHead(data)
        else:
            while pointer.next != None:
                pointer = pointer.next
            pointer.setData(data)

    def reverse(self):
        stack = []
        pointer = self.head
        reverse_list = SinglyLinkedList()
        while pointer.next != None:
            stack.append(pointer.getData())
            pointer = pointer.next
        while len(stack) > 0:
            reverse_list.insert(stack.pop())


’’’
built in node methods
getData
setData
setNext
’’’
