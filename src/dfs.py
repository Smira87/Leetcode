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
    def DFSUtil(self, s, v, visited):

        # Mark all the vertices as not visited

        # Create a queue for BFS

        # Mark the source node as
        # visited and enqueue it

        visited[s] = True

        for i in self.graph[s]:
            if i == v:
                return True

            if i not in visited:
                visited[i] = True

                if self.DFSUtil(i, v, visited):
                    return True


        return False

    def DFS(self, s, v):

        visited = {}

        return self.DFSUtil(s, v, visited)

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


print(g.DFS(2, 5))
