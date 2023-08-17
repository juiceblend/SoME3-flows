from manim import *
import numpy as np
from make_network import *

class FordFulkersonExample(Scene):
    
    def construct(self):

        # Animation 1 - Fade chapter intro
        n = 7
        r = 0.5
        show_cap = True

        # adjacency matrix - see make_network.py

        adj_mat = np.array([ 
            [0, 8, 9, 5, 0, 0, 0], 
            [0, 0, 0, 0, 6, 0, 0], 
            [0, 0, 0, 7, 0, 5, 0], 
            [0, 1, 0, 0, 2, 6, 0], 
            [0, 0, 0, 0, 0, 0, 11], 
            [0, 0, 0, 0, 4, 0, 13], 
            [0, 0, 0, 0, 0, 0, 0]  
        ])

        # positions of nodes - see make_network.py

        pos = np.array([ 
            [ -5, -2.5, -2.5,   0,  2.5,  2.5,   5], 
            [  0,    3,   -3,   0,    3,   -3,   0], 
            [  0,    0,    0,   0,    0,    0,   0] 
        ])
        
        network = MakeNetwork(n, r, pos, adj_mat, show_capacity=show_cap, highlight_endpoints=True)
        Nodes = network.Nodes
        Edges = network.Edges
        edge_endpts = network.edge_endpts

        # Draw network

        # start at t=1
        self.play(Write(VGroup(Nodes, Edges)), run_time = 3)
        self.wait(60)

        # Indicate path to augment
        # t=64
        path1 = [[0,1], [1,4], [4,6]]
        animations_1 = network.AugmentPath(path1, amount=0)
        self.play(*animations_1, run_time=2)
        self.wait(33)
        

        # Augment by 1
        # t=99
        animations_2 = network.AugmentPath(path1, amount=1)
        self.play(*animations_2, run_time=2)
        self.wait(20)

        # Augment by 6
        # t=121
        animations_3 = network.AugmentPath(path1, amount=5)
        self.play(*animations_3, run_time=2)
        self.wait(23)

        # Augment bottom path
        # t=146
        path2 = [[0,2], [2,5], [5,6]]
        animations_4 = network.AugmentPath(path2, amount=5)
        self.play(*animations_4, run_time=2)
        self.wait(30)

        # Augment a bunch of paths quickly
        # t=178
        path3 = [[0,2], [2,3], [3,5], [5, 6]]
        animations_5 = network.AugmentPath(path3, amount=4)
        self.play(*animations_5, run_time=0.8)
        self.wait(0.3)

        path4 = [[0, 3], [3, 4], [4, 6]]
        animations_6 = network.AugmentPath(path4, amount=2)
        self.play(*animations_6, run_time=0.8)
        self.wait(0.3)
        
        path5 = [[0, 3], [3, 5], [5, 6]]
        animations_7 = network.AugmentPath(path5, amount=2)
        self.play(*animations_7, run_time=0.8)
        self.wait(100)





