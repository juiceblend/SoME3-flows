from collections import defaultdict

class GraphNet:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False] * self.ROW
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False

    def FordFulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0
        path = []

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            current_path = []
            v = sink
            while v != source:
                u = parent[v]
                current_path.append([u, v])  # Store the edge in the path
                self.graph[u][v] = max(self.graph[u][v] - path_flow, 0)
                self.graph[v][u] += path_flow
                v = parent[v]
            path.append(current_path)  # Store the current path

            max_flow += path_flow

        return max_flow, path  # Return the maximum flow and the list of paths