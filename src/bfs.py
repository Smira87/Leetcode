from collections import defaultdict
from collections import deque


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s, v):

        # Mark all the vertices as not visited
        visited = {}

        # Create a queue for BFS
        queue = deque([[s, 1]])

        # Mark the source node as
        # visited and enqueue it

        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s, level = queue.popleft()
            print(s, end=" level " + str(level) + " ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if i not in visited:
                    queue.append([i, level + 1])
                    visited[i] = True
                if i == v:
                    return level + 1

        return False


# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(3, 5)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
print(g.BFS(2, 6))
