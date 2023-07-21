from manim import *
import numpy as np
from network import *

class Cards(Scene):

    def construct(self):

        # First initialize nodes
        start = Node([-5,0,0], 'A')
        end = Node([5,0,0], 'B')

        piles = [0]*13
        suits = [0]*13

        for i in range(13):
            piles[i] = Node([-2,-3 + i/2,0], str(i))
            suits[i] = Node([2,-3 + i/2,0], str(i))
        
        # Inialize edges
        edge_list = []

        # only display capacity on the bottom edge
        edge_list.append(Edge(start, piles[0], 1, display_capacity = True))
        edge_list.append(Edge(suits[0], end, 1, display_capacity = True))
        edge_list.append(Edge(piles[0], suits[0], 9, display_capacity = True))

        for i in range(1,13):
            edge_list.append(Edge(start, piles[i], 1))
            edge_list.append(Edge(suits[i], end, 1))
            edge_list.append(Edge(piles[i], suits[i], 9))


        # Initialize graph
        graph = Network([start] + piles + suits + [end], edge_list)
        
        
        # Convert to manim
        Nodes, Edges = graph.to_VGroup()
    
        self.play(Write(VGroup(Nodes, Edges)), run_time = 3)
        self.wait(1)