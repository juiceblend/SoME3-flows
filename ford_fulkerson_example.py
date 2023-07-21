from manim import *
import numpy as np
from make_network import *

class FordFulkersonExample(Scene):

    def construct(self):
        
        n = 7
        r = 0.3

        adj_mat = np.array([ 
            [0, 1, 1, 1, 0, 0, 0], 
            [0, 0, 0, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 1, 0], 
            [0, 1, 0, 0, 1, 1, 0], 
            [0, 0, 0, 0, 0, 0, 1], 
            [0, 0, 0, 0, 1, 0, 1], 
            [0, 0, 0, 0, 0, 0, 0]  
        ])

        pos = np.array([ 
            [ -5, -2.5, -2.5,   0,  2.5,  2.5,   5], 
            [  0,    3,   -3,   0,    3,   -3,   0], 
            [  0,    0,    0,   0,    0,    0,   0] 
        ])
        
        network = MakeNetwork(n, r, pos, adj_mat)
        Nodes = network.Nodes
        Edges = network.Edges
        edge_endpts = network.edge_endpts
    
        self.play(Write(VGroup(Nodes, Edges)), run_time = 3)
        self.wait(1)

        path1 = [[0,1], [1,4], [4,6]]
        animations_1 = network.AugmentPath(path1, Edges, edge_endpts)
        anim_group_1 = AnimationGroup(*animations_1)
        self.play(AnimationGroup(anim_group_1, run_time=2, lag_ratio = 0.2))
