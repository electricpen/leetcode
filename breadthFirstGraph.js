class Node {
  constructor(value) {
    self.data = value;
    self.edges = [];
    self.status = "unvisited";
  }

  addEdge(node) {
    self.edges.push(node);
  }

  getEdges() {
    return self.edges;
  }

  setStatus(status) {
    self.status = status;
  }
}

class Queue {
  constructor() {
    self.storage = [];
  }

  enqueue(data) {
    self.storage.push(data);
  }

  dequeue() {
    return self.storage.shift();
  }

  size() {
    return self.storage.length;
  }
}

const breadthFirstSearch = (vertex, callback) => {
  let queue = new Queue();
  queue.enqueue(vertex);
  while (queue.size > 0) {
    let current = queue.dequeue();
    callback(current);
    for (edge of current) {
      queue.enqueue(edge);
    }
  }
};
