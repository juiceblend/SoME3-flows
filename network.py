from re import I
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
            'R' : 0.5,
            'fill_color': GREEN
        }
        init_values.update(kwargs)

        self.pos = pos
        self.label = label
        self.in_S = init_values['in_S']
        self.R = init_values['R']
        self.fill_color = init_values['fill_color']

    def to_VGroup(self):
        node_text = Tex(self.label)
        node = Dot(point = self.pos, radius = self.R, fill_opacity = 0.3, color = self.fill_color)
        node.move_to(self.pos)
        node_text.move_to(node.get_center())

        node_group = VGroup(node_text, node)

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

        # Define numpy vectors for quantities that will be used later

        self.start_pos = np.array(self.start_node.pos)
        self.end_pos = np.array(self.end_node.pos)
        self.midpt = 0.5*(self.start_pos + self.end_pos) # midpoint of the edge

        '''
        Gets the normal to the edge.
        This isn't particularly important - just helps make some things more readable/look better 
        '''

        R = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]) # rotate pi/2
        normal = (R @ (self.end_pos - self.start_pos)) # get normal to edge by rotating vector by pi/2
        self.unit_normal =  normal/np.linalg.norm(normal)

        self.capacity = capacity

        # default initialization values for Keyword arguments
        init_values = {
            'buff': end_node.R + (np.linalg.norm(self.end_pos - self.start_pos)/10),
            'display_capacity': False,
            'current_flow': 0,
            'arrow_color': "WHITE"
        }
        init_values.update(kwargs)

        self.buff = init_values['buff']
        self.display_capacity = init_values['display_capacity']
        self.current_flow = init_values['current_flow']
        self.arrow_color = init_values['arrow_color']


    def to_VGroup(self):

        #TODO: 
        # - different color/display for current_flow != 0 
        # - different color/display for current_flow != 0
        # - Make capacity display position adjustable/more clear? 
        buff_start = self.start_pos + (RIGHT * self.start_node.R)
        buff_end = self.end_pos + (LEFT * self.start_node.R)

        #edge = Arrow(start = buff_start, end = buff_end, stroke_width=2)
        edge = Arrow(start = self.start_pos, end = self.end_pos, buff = self.buff, color = self.arrow_color, stroke_width = 0.7, tip_length = 0.1)

        '''
        To adjust the position of the capacity, we go out in a normal direction to the edge
        Also adjust font size
        '''

        if 0 < self.current_flow and self.current_flow < self.capacity:
            self.arrow_color = 'GOLD'
        elif self.current_flow == self.capacity:
            self.arrow_color = 'RED'
        else:
            self.arrow_color = 'WHITE'
        

        #edge = Arrow(start = self.start_pos, end = self.end_pos, buff = self.buff, color = self.arrow_color)

        flow_text = Tex(str(self.current_flow), color = WHITE).scale(0.8)
        flow_text.move_to(self.midpt + 0.5*self.unit_normal)

        if self.display_capacity:
            edge_text = Tex(str(self.capacity), color = RED).scale(0.6) # adjust font size
            edge_text.move_to(self.midpt - 0.5*self.unit_normal) # set position of capacity text relative to the edge
            edge_group = VGroup(edge_text, edge, flow_text)
        else:
            edge_group = edge

        return edge_group


