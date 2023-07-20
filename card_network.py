from manim import *
import numpy as np
from network import *

class Cards(Scene):

    def construct(self):

        start = Node([-5,0,0], 'A')
        end = Node([5,0,0], 'B')

        piles = [0]*13
        suits = [0]*13

        for i in range(13):
            piles[i] = Node([-2,-3 + i/2,0], str(i))
            suits[i] = Node([2,-3 + i/2,0], str(i))

        graph = Network([start] + piles + suits + [end])

        for i in range(13):
            graph.add_edge(start, piles[i])
            graph.add_edge(suits[i], end)
            for j in range(13):
                graph.add_edge(piles[i], suits[j])
        
        Nodes, Edges = graph.to_manim()
    
        self.play(Write(VGroup(Nodes, Edges)), run_time = 3)
        self.wait(1)