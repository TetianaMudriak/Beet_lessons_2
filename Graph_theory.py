from collections import defaultdict
from queue import Queue


# Kosaraju's algorithm to find strongly connected components in Python

class Graph:

    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.vertex)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print strongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * self.vertex

        for i in range(self.vertex):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * self.vertex

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")

    def bfs(self, start_vertex, target_vertex):
        # Set of visited vertexes to prevent loops
        visited = set()
        queue = Queue()

        # Add the start_vertex to the queue and visited list
        queue.put(start_vertex)
        visited.add(start_vertex)

        # start_vertex has not parents
        parent = dict()
        parent[start_vertex] = None

        # Perform step 3
        path_found = False
        while not queue.empty():
            current_vertex = queue.get()
            if current_vertex == target_vertex:
                path_found = True
                break

            for next_vertex in self.graph[current_vertex]:
                if next_vertex not in visited:
                    queue.put(next_vertex)
                    parent[next_vertex] = current_vertex
                    visited.add(next_vertex)

        # Path reconstruction
        path = []
        if path_found:
            path.append(target_vertex)
            while parent[target_vertex] is not None:
                path.append(parent[target_vertex])
                target_vertex = parent[target_vertex]
            path.reverse()
        return path


def main():
    # Task 1
    # Kosaraju's algorithm
    graph = Graph(7)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(5, 3)

    print("Strongly Connected Components:")
    graph.print_scc()

    # Task 2
    # Breadth first search the shortest path
    graph2 = Graph(4)
    graph2.add_edge(0, 1)
    graph2.add_edge(0, 2)
    graph2.add_edge(1, 3)
    graph2.add_edge(3, 2)
    graph2.add_edge(3, 0)
    print(graph2.bfs(0, 3))
    print(graph2.bfs(0, 2))
    print(graph2.bfs(1, 2))
    print(graph.bfs(0, 5))


if __name__ == '__main__':
    main()
