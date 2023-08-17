from manim import *
import numpy as np
from make_network import *

class Cut(Scene):
    def construct(self):

        # ---------------------- Setup ----------------------

        n = 7
        r = 0.5

        adj_mat = np.array([ 
            [0, 8, 9, 5, 0, 0, 0], 
            [0, 0, 0, 0, 6, 0, 0], 
            [0, 0, 0, 7, 0, 5, 0], 
            [0, 1, 0, 0, 2, 6, 0], 
            [0, 0, 0, 0, 0, 0, 11], 
            [0, 0, 0, 0, 4, 0, 13], 
            [0, 0, 0, 0, 0, 0, 0]  
        ])

        pos = np.array([ 
            [ -5, -2.5, -2.5,   0,  2.5,  2.5,   5], 
            [  0,    3,   -3,   0,    3,   -3,   0], 
            [  0,    0,    0,   0,    0,    0,   0] 
        ])
        
        network = MakeNetwork(n, r, pos, adj_mat, show_capacity=True, highlight_endpoints = True)
        Nodes = network.Nodes
        Edges = network.Edges

        S_text = Tex("S")
        T_text = Tex("T")   
        S_text.shift(UP*2.9 + LEFT * 4.5).scale(1.5)
        T_text.shift(UP*2.9 + RIGHT * 4.5).scale(1.5)
        S_text.set_color(GREEN)
        T_text.set_color(BLUE)

        net_flow_text = Tex("Net flow ", "through cut = Total flow through network")
        net_flow_text[0].set_color(YELLOW)
        net_flow_text.shift(UP*3.5)

        capacity_A_add_text = Tex("Cut Capacity = ","6","+","5","+","7","+",r"5\ ","= 23")
        capacity_A_add_text.shift(UP*3.5)

        capacity_B_text = Tex("Cut Capacity = ","6","+","2","+","6","+",r"5\ ","= 19")
        capacity_B_text.shift(UP*3.5)

        cut_A_endpoints = [[1,4],[3,1],[0,3],[2,3],[2,5]]
        cut_A_forward_endpoints = [[1,4],[0,3],[2,3],[2,5]]
        cut_B_endpoints = [[1, 4], [3, 4], [3, 5], [2, 5]]
        


        # ---------------------- Animation ----------------------

        self.play(Write(VGroup(Nodes, Edges)), run_time = 3)
        self.wait(1)

        cut_A_object = network.DrawCut(cut_A_endpoints)
        self.play(Create(cut_A_object))

        self.play(AnimationGroup(*[
            Nodes[1].animate.set_color(GREEN), 
            Nodes[2].animate.set_color(GREEN),
            Nodes[3].animate.set_color(BLUE),
            Nodes[4].animate.set_color(BLUE),
            Nodes[5].animate.set_color(BLUE),
            FadeIn(S_text),
            FadeIn(T_text)], run_time=1, lag_ratio = 0))
        
        self.wait(2)

        diagram = VGroup(Nodes, Edges, cut_A_object, S_text, T_text)
        self.play(diagram.animate.scale(0.8).shift(DOWN))
        self.play(Write(net_flow_text))
        self.play(AnimationGroup(*network.WiggleEdges(cut_A_endpoints), run_time=2, lag_ratio = 0.1))
        self.wait(2)
        self.play(FadeOut(net_flow_text))
        self.wait(1)


        self.play(Write(capacity_A_add_text[0]))
        self.wait(1)
        for i in range(len(cut_A_forward_endpoints)):
            self.play(AnimationGroup(*[
                Indicate(network.Edges[network.edge_endpts.index(cut_A_forward_endpoints[i])]), 
                Indicate(capacity_A_add_text[1+2*i])
                ], run_time=0.8, lag_ratio = 0))
            self.play(Write(capacity_A_add_text[2+2*i]), run_time=0.5)

        self.wait(2)

        cut_B_object = network.DrawCut(cut_B_endpoints).scale(0.8)
        cut_B_object.shift(DOWN)
        

        self.play(AnimationGroup(*[
            Transform(cut_A_object, cut_B_object),
            Nodes[3].animate.set_color(GREEN), 
            Transform(capacity_A_add_text[1], capacity_B_text[1]),
            Transform(capacity_A_add_text[3], capacity_B_text[3]),
            Transform(capacity_A_add_text[5], capacity_B_text[5]),
            Transform(capacity_A_add_text[7], capacity_B_text[7]),
            Transform(capacity_A_add_text[8], capacity_B_text[8])
            ], run_time=2, lag_ratio = 0))
        
        self.wait(2)