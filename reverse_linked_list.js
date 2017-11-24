class Node {
  constructor(data = null) {
    this.data = data;
    this.next = null;
  }

  setData(data) {
    this.data = data;
  }

  setNext(node) {
    this.next = node;
  }

  getData() {
    return this.data;
  }
}

class LinkedList {
  constructor() {
    this.head = new Node();
  }

  setHead(data) {
    this.head = new Node(data);
  }

  insert(data) {
    let newNode = new Node(data);
    let current = this.head;
    while (current.next !== null) {
      current = current.next;
    }
    current.next = newNode;
  }

  reverse() {
    let last = null;
    let current = this.head;
    while (current !== null) {
      next = current.next;
      current.next = last;
      last = current;
      current = next;
    }
    this.setHead(last.getData());
  }
}
