from manim import *
import numpy as np
from make_network import *

class BasicExample(Scene):

    def construct(self):
        
        '''
        n = number of nodes
        r = radius of the node
        show_cap = show capacity?
        '''

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
        
        network = MakeNetwork(n, r, pos, adj_mat, show_capacity=show_cap)
        Nodes = network.Nodes
        Edges = network.Edges
        edge_endpts = network.edge_endpts

        # draw network

        self.play(Write(VGroup(Nodes, Edges)), run_time = 3)
        self.wait(1)

        '''
        To highlight a path, make a list with the endpoints of the edges that are being highlighted
        Pass this to AugmentPath()
        (See make_network.py)
        '''

        path1 = [[0,1], [1,4], [4,6]]
        animations_1 = network.AugmentPath(path1)
        anim_group_1 = AnimationGroup(*animations_1)
        self.play(AnimationGroup(anim_group_1, run_time=2, lag_ratio = 0.2))

        self.wait(2)

        '''
        To draw a cut, make a list with the endpoints of the edges through which the cut should pass
        Pass this to DrawCut() 
        (See make_network.py)
        '''

        cut_1 = network.DrawCut([[1, 4], [3, 4], [3, 5], [2, 5]])
        self.play(Create(cut_1))
        
        self.wait(2)
