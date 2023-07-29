from manim import *
import numpy as np
from network import *

class MakeNetwork:

    def __init__(self, n, r, node_positions, adj_mat, show_capacity = False):
        '''
        Inputs: 
        n = number of nodes
        r = radius
        node_positions is a 3xn array where the i-th column is the position of the i-th node
        adj_mat is the adjacency matrix, adj[i,j] = capacity[i,j] if there is edge from i to j and adj[i,j] = 0 otherwise
        '''

        nodes = []
        edge_list = []
        edge_endpts = []

        for i in range(n):
            nodes.append(Node(node_positions[:, i], str(i), R = r))

        for i in range(n):
            for j in range (n):
                if adj_mat[i,j] > 0:
                    edge_list.append(Edge(nodes[i], nodes[j], adj_mat[i,j], display_capacity = show_capacity))
                    edge_endpts.append([i, j])
        
        graph = Network(nodes, edge_list)

        self.Nodes, self.Edges = graph.to_VGroup()
        self.edge_endpts = edge_endpts
    
    def AugmentPath(self, path):

        indices = [self.edge_endpts.index(u) for u in path]  
        animations = [Indicate(self.Edges[k]) for k in indices]
        
        return animations