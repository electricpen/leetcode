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

const breadthFirstSearch = vertex => {};
