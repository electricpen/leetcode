class MinHeap {
  constructor(props) {
    this.storage = [];
  }

  swap(a, b) {
    const temp = this.storage[a];
    this.storage[a] = this.storage[b];
    this.storage[b] = temp;
  }

  getParent(index) {
    return this.storage[Math.floor((index + 1) / 2)];
  }

  getLeftChild(index) {
    return this.storage[(index + 1) * 2];
  }

  getRightChild(index) {
    return this.storage[(index + 1) * 2 + 1];
  }

  heapifyUp(index) {
    // if current is smaller than parent, swap
    // recurse on parent index
  }

  heapifyDown(index) {
    const c1 = (index + 1) * 2 - 1;
    const c2 = (index + 1) * 2 + 1 - 1;

    if (c1 < this.size() && this.storage[index] > this.storage[c1]) {
      this.swap(index, c1);
      this.heapifyDown(c1);
    } else if (c2 < this.size() && this.storage[index] > this.storage[c2]) {
      this.swap(index, c2);
      this.heapifyDown(c2);
    }
  }

  insert(data) {
    this.storage.push(data);
    this.heapifyUp(this.storage.length - 1);
  }

  pop() {
    const min = this.storage[0];
    const end = this.storage.pop();
    this.storage[0] === end;
    this.heapifyDown(0);
    return min;
  }

  size() {
    return this.storage.length;
  }

  getMin() {
    return this.storage[0];
  }
}

class MaxHeap {
  constructor(props) {
    this.storage = [];
  }
  swap(a, b) {
    const temp = this.storage[a];
    this.storage[a] = this.storage[b];
    this.storage[b] = temp;
  }

  getParent(index) {
    return this.storage[Math.floor((index + 1) / 2)];
  }

  getLeftChild(index) {
    return this.storage[(index + 1) * 2];
  }

  getRightChild(index) {
    return this.storage[(index + 1) * 2 + 1];
  }

  heapifyUp(index) {}

  heapifyDown(index) {}

  insert(data) {
    this.storage.push(data);
    this.heapifyUp(this.storage.length - 1);
  }

  pop() {
    const max = this.storage[0];
    const end = this.storage.pop();
    this.storage[0] = end;
    this.heapifyDown(0);
    return max;
  }

  size() {
    return this.storage.length;
  }

  getMax() {
    return this.storage[0];
  }
}

class medianStream {
  constructor(props) {
    this.bigHeap = new MinHeap();
    this.smallHeap = new MaxHeap();
  }

  insert(data) {
    if (data < this.peekMedian()) {
      this.smallHeap.insert(data);
    } else {
      this.bigHeap.insert(data);
    }

    if (this.bigHeap.size() - this.smallHeap.size() > 1) {
      this.smallHeap.insert(this.bigHeap.pop());
    } else if (this.smallHeap.size() - this.bigHeap.size() > 1) {
      this.bigHeap.insert(this.smallHeap.pop());
    }
  }

  peekMedian() {
    if (this.bigHeap.size() === 0 && this.smallHeap.size() === 0) {
      return null;
    }
    if (this.bigHeap.size() > this.smallHeap.size()) {
      return this.bigHeap.getMin();
    } else if (this.smallHeap.size() > this.bigHeap.size()) {
      return this.smallHeap.getMax();
    } else {
      return (this.bigHeap.getMin() + this.smallHeap.getMax()) / 2;
    }
  }

  size() {
    return this.bigHeap.size() + this.smallHeap.size();
  }
}
