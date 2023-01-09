// graphs are a series of nodes that are represented by an object called an
// 'adjacency list' which defines which node can be reached by another, or the
// graph's 'edges'

// first thing we might do is a traversal
// depth first traversal will go in one direction until it has to change directions

// breadth first traversal goes to each neighbor first in a even direction

const graph = {
  a: ["b", "c"],
  b: ["d"],
  c: ["e"],
  d: ["f"],
  e: [],
  f: [],
};

const depthFirstPrint = (graph, start) => {
  console.log("\nDepth First Print ");
  const stack = [start];
  while (stack.length > 0) {
    let current = stack.pop();
    console.log(current);
    for (let neighbor of graph[current]) {
      stack.push(neighbor);
    }
  }
};

const recursiveDepthFirstPrint = (graph, start) => {
  console.log(start);
  for (neighbor of graph[start]) {
    recursiveDepthFirstPrint(graph, neighbor);
  }
};

console.log("recursive depth first print");
recursiveDepthFirstPrint(graph, "a");
depthFirstPrint(graph, "a");

const breadthFirstPrint = (graph, start) => {
  console.log("\nBreadth First Print ");
  const queue = [start];
  while (queue.length > 0) {
    const current = queue.shift();
    console.log(current);
    for (let neighbor of graph[current]) {
      queue.push(neighbor);
    }
  }
};

breadthFirstPrint(graph, "a");
// "seems simple enough" he said, not knowing this would drive him to madness
