from tracemalloc import start
from manim import *
import numpy as np

class Network:
    '''
    Implements a graph of Node and Edge objects
    Nodes are stored in a dictionary where each Node acts as a key for all its outgoing edges
    '''

    def __init__(self, nodes = [], edges = []):
        '''
        Args:
            nodes    ([Node]): array of Nodes in the network
            edges    ([Edge]): array of Edges in the network
        '''

        self.edges = edges

        self.graph = {}
        for node in nodes:
            self.graph[node] = set()
            for edge in self.edges:
                if edge.start_node == node:
                    self.graph[node].add(edge)

        self.size = len(self.graph)


    def add_node(self, node, **kwargs):
        # implement if needed

        '''
        Keyword Args:
            in_nodes    ([Node]): array of nodes with edges going into the new node
            out_nodes   ([Node]): array of nodes with edges going out of the new node
        '''
        adj_edges = {
            'in_nodes' : [],
            'out_nodes' : []
        }
        adj_edges.update(kwargs)

        return
    
    def add_edge(self, edge): 
        # implement if needed            
        return

    def to_VGroup(self):
        # output Vgroups for Nodes, Edges

        Nodes = VGroup()
        Edges = VGroup()

        for node in self.graph:
            Nodes = Nodes.add(node.to_VGroup())
        
        for edge in self.edges:
            Edges.add(edge.to_VGroup())

        return Nodes, Edges


class Node:
    def __init__(self, pos: list, label: str, **kwargs):
        '''
        Args:
            pos        ([arr]): coords of Node, given as [x,y,z]
            label        (str): label displayed in animation

        Keyword Args:
            in_S         (int): is 1 if node is in S, -1 if node is in Sbar, 0 otherwise.
            R          (float): radius of drawn circle
            fill_color (color): fill_color
        '''

        # default initialization values for Keyword arguments
        init_values = {
            'in_S' : 0,
            'R' : 0.3,
            'fill_color': RED
        }
        init_values.update(kwargs)

        self.pos = pos
        self.label = label
        self.in_S = init_values['in_S']
        self.R = init_values['R']
        self.fill_color = init_values['fill_color']

    def to_VGroup(self):
        node_text = Tex(self.label)
        node = Circle(radius = self.R, fill_color = self.fill_color, fill_opacity = 0.4).surround(node_text)

        node_group = VGroup(node_text, node)
        node_group.move_to(self.pos)

        return node_group
    


class Edge:
    def __init__(self, start_node: Node, end_node: Node, capacity: int, **kwargs):
        '''
        Args:
            start_node   (Node): starting Node
            end_node     (Node): ending Node
            capacity      (int): capacity of edge

        Keyword Args:
            display_capacity (bool): controls whether the capacity is displayed underneath the edge
            current_flow      (int): current flow through the edge
            buff            (float): not sure what this does
        '''

        self.start_node = start_node
        self.end_node = end_node
        self.capacity = capacity

        # default initialization values for Keyword arguments
        init_values = {
            'buff': end_node.R + (np.linalg.norm(np.array(end_node.pos) - np.array(start_node.pos))/10),
            'display_capacity': False,
            'current_flow': 0
        }
        init_values.update(kwargs)

        self.buff = init_values['buff']
        self.display_capacity = init_values['display_capacity']
        self.current_flow = 0

    def to_VGroup(self):

        #TODO: 
        # - different color/display for current_flow != 0
        # - Make capacity display position adjustable/more clear? 

        start_pos = np.array(self.start_node.pos)
        end_pos = np.array(self.end_node.pos)

        edge = Arrow(start = start_pos, end = end_pos, buff = self.buff)

        R = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
        midpt = 0.5*(start_pos + end_pos)
        normal = (R @ (end_pos-start_pos))
        unit_normal =  normal/np.linalg.norm(normal)
        

        if self.display_capacity:
            edge_text = Tex(str(self.capacity)).scale(0.8)
            edge_text.move_to(midpt + 0.5*unit_normal)
            edge_group = VGroup(edge_text, edge)
        else:
            edge_group = edge

        return edge_group


