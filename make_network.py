from manim import *
import numpy as np
from network import *

class MakeNetwork:

    def __init__(self, n, r, node_positions, adj_mat, show_capacity = False, **kwargs):
        '''
        Inputs: 
        n = number of nodes
        r = radius
        node_positions is a 3xn array where the i-th column is the position of the i-th node
        adj_mat is the adjacency matrix, adj[i,j] = capacity[i,j] if there is edge from i to j and adj[i,j] = 0 otherwise
        '''

        self.n = n
        self.r = r
        self.node_positions = node_positions
        self.adj_mat = adj_mat
        self.show_capacity = show_capacity
        init_values = {
            'labels' : [i for i in range(n)],
            'highlight_endpoints' : False
        }
        init_values.update(kwargs)

        self.labels = init_values['labels']
        self.highlight_endpoints = init_values['highlight_endpoints']

        nodes = []
        edge_list = []
        edge_endpts = []

        if self.highlight_endpoints:
            nodes.append(Node(self.node_positions[:, 0], str(self.labels[0]), R = self.r, fill_color = GREEN))
            for i in range(1,self.n-1):
                nodes.append(Node(self.node_positions[:, i], str(self.labels[i]), R = self.r))
            nodes.append(Node(self.node_positions[:, self.n-1], str(self.labels[self.n-1]), R = self.r, fill_color = BLUE))
        else:
            nodes.append(Node(self.node_positions[:, 0], str(self.labels[0]), R = self.r))
            for i in range(1,self.n-1):
                nodes.append(Node(self.node_positions[:, i], str(self.labels[i]), R = self.r))
            nodes.append(Node(self.node_positions[:, self.n-1], str(self.labels[self.n-1]), R = self.r))
        

        for i in range(self.n):
            for j in range (self.n):
                if self.adj_mat[i,j] > 0:
                    edge_list.append(Edge(nodes[i], nodes[j], self.adj_mat[i,j], display_capacity = self.show_capacity))
                    edge_endpts.append([i, j])
        
        self.graph = Network(nodes, edge_list)

        self.Nodes, self.Edges = self.graph.to_VGroup()
        self.edge_endpts = edge_endpts
    
    def AugmentPath(self, path, amount):

        indices = [self.edge_endpts.index(u) for u in path]  # given the endpoints, find the index of the endpoints in edge_endpts
        anims = []
        
        for k in indices:
            anims.append(Indicate(self.Edges[k][1]))
            e = self.graph.edges[k]
            new_edge = Edge(e.start_node, e.end_node,capacity=e.capacity, display_capacity = e.display_capacity, current_flow = e.current_flow + amount, buff = e.buff)
            new_edge_mobject = new_edge.to_VGroup()
            anims.append( FadeTransform(self.Edges[k][2], new_edge_mobject[2]) )
            self.Edges[k][1].become(new_edge_mobject[1])

            e.current_flow += amount
            self.Edges[k][2] = new_edge_mobject[2]

        return anims

        """ return highlight_anim """
    
    def WiggleEdges(self, edges):

        indices = [self.edge_endpts.index(u) for u in edges]  
        animations = [Wiggle(self.Edges[k]) for k in indices]
        
        return animations
    
    def DrawCut(self, endpt_list):
        indices = [self.edge_endpts.index(u) for u in endpt_list] # given the endpoints, find the index of the endpoints in edge_endpts
        edge_list = [self.graph.edges[k] for k in indices] # use the index to get the actual edge
        midpt_list = [edge.midpt for edge in edge_list] # get the midpoint of each edge

        '''
        midpt_list is the list of points through which the cut should pass (midpoints of the corresponding edges)
        We just add two points on either side so it looks nicer
        '''

        initial_pt = edge_list[0].midpt + 0.3 * edge_list[0].unit_normal
        end_pt = edge_list[-1].midpt - 0.3 * edge_list[-1].unit_normal

        midpt_list = [initial_pt] + midpt_list + [end_pt]

        curve = VMobject()
        curve.set_points_smoothly(midpt_list)
        curve = DashedVMobject(curve, num_dashes = 30, equal_lengths = True)

        return curve