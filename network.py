from manim import *
import numpy as np

class Network:
    '''
    Implements a graph of Node objects as a dictionary
    https://www.tutorialspoint.com/python_data_structure/python_graphs.htm
    '''

    def __init__(self, nodes = []):
        '''
        Takes as argument a list of nodes
        '''

        self.graph = {}
        for node in nodes:
            self.graph[node] = set()

        self.size = len(self.graph)


    def add_node(self, node, **kwargs):
        '''
        Takes optional arguments
        in_nodes: array of nodes
        out_nodes: array of nodes
        '''
        adj_edges = {
            'in_nodes' : [],
            'out_nodes' : []
        }
        adj_edges.update(kwargs)

        self.graph[node] = set(adj_edges['out_nodes'])

        for in_node in adj_edges['in_nodes']:
            self.graph[in_node].add(node)
        
        self.size = self.size + 1
    
    def add_edge(self, start_node, end_node) -> bool: 

        if start_node in self.graph:
            self.graph[start_node].add(end_node)
            return True

        return False

    def to_manim(self):
        # output Vgroups for Nodes, Edges

        Nodes = VGroup()
        Edges = VGroup()

        for node in self.graph:
            Nodes = Nodes.add(node.to_manim())
            for out_node in self.graph[node]:
                # TODO: make this edge weight adjustable
                edge = Arrow(start = node.pos, end = out_node.pos, buff = 0.1)
                Edges.add(edge)

        return Nodes, Edges


class Node:
    def __init__(self, pos: list, label: str, **kwargs):
        '''
        Takes as optional arguments
        in_S: is 1 if node is in S, -1 if node is in Sbar, 0 otherwise.
        R: radius of drawn circle
        fill_color: fill_color
        '''

        self.pos = pos
        self.label = label

        # default initialization values
        init_values = {
            'in_S' : 0,
            'R' : 0.3,
            'fill_color': RED
        }
        init_values.update(kwargs)

        self.in_S = init_values['in_S']
        self.R = init_values['R']
        self.fill_color = init_values['fill_color']

    def to_manim(self):
        node_text = Tex(self.label)
        node = Circle(radius = self.R, fill_color = self.fill_color, fill_opacity = 0.4).surround(node_text)

        node_group = VGroup(node_text, node)
        node_group.move_to(self.pos)

        return node_group

