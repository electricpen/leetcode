class MinHeap {
  constructor(props) {
    this.storage = [];    
  }

  insert(data) {

  }

  size() {
    return this.storage.length;
  }
}

class MaxHeap {
  constructor(props) {
    this.storage = [];    
  }
  
  insert(data) {

  }

  size() {
    return this.storage.length;
  }
}

class medianStream {
  constructor(props) {
    this.topHalf = new MinHeap;
    this.bottomHalf = new MaxHeap;
  }

  insert(data) {

  }

  peekMedian() {

  }

  size() {

  }
}