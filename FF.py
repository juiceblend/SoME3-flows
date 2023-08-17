def ford_fulkerson(graph, source, sink):
    def bfs(graph, parent):
        visited = [False] * len(graph)
        queue = [source]
        visited[source] = True
        
        while queue:
            current_node = queue.pop(0)
            for node, capacity in enumerate(graph[current_node]):
                if not visited[node] and capacity > 0:
                    queue.append(node)
                    parent[node] = current_node
                    visited[node] = True
        return visited[sink]
    
    def find_path(parent):
        path = []
        node = sink
        while node != -1:
            path.insert(0, node)
            node = parent[node]
        return path
    
    max_flow = 0
    parent = [-1] * len(graph)
    paths_used = []
    
    while bfs(graph, parent):
        path = find_path(parent)
        min_capacity = float('inf')
        
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            min_capacity = min(min_capacity, graph[u][v])
            
        max_flow += min_capacity
        paths_used.append(path)
        
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            graph[u][v] -= min_capacity
            graph[v][u] += min_capacity
            
    edge_paths_used = []
    for path in paths_used:
        edge_path = [[path[i], path[i + 1]] for i in range(len(path) - 1)]
        edge_paths_used.append(edge_path)
            
    return max_flow, edge_paths_used
