from manim import *
from make_network import *
from Deal import *
import numpy as np
from FF import *
from Deck import *

class Trick(Scene):
    def construct(self):
        inf = float("inf")

        pos = np.array([[-6.5, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 6.5], 
               [0, 3.600000000000001, 3.000000000000001, 2.4000000000000012, 1.8000000000000012, 1.200000000000001, 0.600000000000001, 5.273559366969494e-16, -0.6, -1.2000000000000006, -1.8000000000000012, -2.4000000000000012, -3.000000000000001, -3.600000000000001, 3.600000000000001, 3.000000000000001, 2.4000000000000012, 1.8000000000000012, 1.200000000000001, 0.600000000000001, 5.273559366969494e-16, -0.6, -1.2000000000000006, -1.8000000000000012, -2.4000000000000012, -3.000000000000001, -3.600000000000001, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        
        adj_mat = np.array([[ 0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0,
   0,  0,  0,  0, inf,  0,  0,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0, inf, inf,
   0,  0,  0,  0,  0,  0, inf,  0,  0,  0],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
  inf, inf, inf,  0, inf,  0,  0,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0, inf,  0,
   0,  0,  0,  0,  0,  0,  0, inf, inf,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0, inf,  0,  0, inf, 0, inf,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0, inf, inf,  0, inf,  0, inf,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,
  inf,  0,  0, inf,  0,  0,  0,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0, inf,  0,  0,  0,  0,  0, inf, inf,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf, inf,  0,  0,
   0, inf,  0,  0,  0, inf,  0,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0,  0,
   0,  0, inf,  0,  0, inf, inf,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0,  0, inf,
  inf,  0,  0,  0, inf,  0,  0,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0, inf,
   0,  0,  0,  0,  0, inf,  0,  0, inf,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0,  0,
   0,  0, inf,  0,  0,  0, inf, inf, 0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,]])
        
        n = 28
        r = 0.3
        show_cap = True

        network = MakeNetwork(n, r, pos, adj_mat)

        Nodes = network.Nodes
        Edges = network.Edges
        edge_endpts = network.edge_endpts

        self.play(Write(VGroup(Nodes, Edges)), run_time = 5)