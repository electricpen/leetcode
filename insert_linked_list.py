class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    # Method for inserting a new node at the start of a Linked List
    def insert_at_front(self, data):
        new_node = Node()
        new_node.setData(data)
        new_node.setNext(self.head)
        self.setHead = new_node


"""
Javascript Implementation
class Node {
  super(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  super() {
    this.head = null;
  }
  setHead(node) {
    this.head = node;
  }
  insertAtHead(data) {
    newNode = new Node(data);
    newNode.next = this.head;
    this.setHead = newNode;
  }
}
"""
