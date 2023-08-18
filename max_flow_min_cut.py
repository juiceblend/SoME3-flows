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

        net_flow_text = Tex("Net flow ", "through cut ","=", " Total flow through network")
        net_flow_text[0].set_color(YELLOW)
        net_flow_text.shift(UP*3.5)

        capacity_flow_text = Tex("Capacity ", "through cut ",r"$\ge$", " Total flow through network")
        capacity_flow_text[0].set_color(YELLOW)
        capacity_flow_text.shift(UP*3.5)

        capacity_equal_text = Tex("Minimum Capacity ",r"=\ ", "Maximum flow")
        capacity_equal_text[0].set_color(YELLOW)
        capacity_equal_text.shift(UP*3.5)


        capacity_A_add_text = Tex("Cut Capacity = ","6","+","5","+","7","+",r"5\ ","= 23")
        capacity_A_add_text.shift(UP*3.5)

        capacity_B_text = Tex("Cut Capacity = ","6","+","2","+","6","+",r"5\ ","= 19")
        capacity_B_text.shift(UP*3.5)

        cut_A_endpoints = [[1,4],[3,1],[0,3],[2,3],[2,5]]
        cut_A_forward_endpoints = [[1,4],[0,3],[2,3],[2,5]]
        cut_B_endpoints = [[1, 4], [3, 4], [3, 5], [2, 5]]
        


        # ---------------------- Animation ----------------------

        self.play(Write(VGroup(Nodes, Edges)), run_time = 3)
        self.wait(11)

        # t=14
        cut_A_object = network.DrawCut(cut_A_endpoints)
        self.play(Create(cut_A_object), run_time=2)
        self.wait(7)

        # t=23
        self.play(AnimationGroup(*[
            Nodes[1].animate.set_color(GREEN), 
            Nodes[2].animate.set_color(GREEN),
            Nodes[3].animate.set_color(BLUE),
            Nodes[4].animate.set_color(BLUE),
            Nodes[5].animate.set_color(BLUE),
            FadeIn(S_text),
            FadeIn(T_text)], run_time=1, lag_ratio = 0))
        self.wait(13)

        # t=37
        self.play(AnimationGroup(*network.WiggleEdges(cut_A_endpoints), run_time=2, lag_ratio = 0.1))
        self.wait(6)

        # t=45
        diagram = VGroup(Nodes, Edges, cut_A_object, S_text, T_text)
        self.play(diagram.animate.scale(0.8).shift(DOWN), run_time=1)
        self.play(Write(net_flow_text), run_time=2)
        self.wait(16)

        # t=64
        self.play(FadeOut(net_flow_text), run_time=1)
        self.wait(1)

        # t=66
        # this chunk takes 8.2s
        self.play(Write(capacity_A_add_text[0]), run_time=2)
        self.wait(1)
        for i in range(len(cut_A_forward_endpoints)):
            self.play(AnimationGroup(*[
                Indicate(network.Edges[network.edge_endpts.index(cut_A_forward_endpoints[i])]), 
                Indicate(capacity_A_add_text[1+2*i])
                ], run_time=0.8, lag_ratio = 0))
            self.play(Write(capacity_A_add_text[2+2*i]), run_time=0.5)

        self.wait(9.3)

        # t=83.5
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
        
        self.wait(4.5)

        # t=89
        self.play(AnimationGroup(*[
            FadeOut(capacity_A_add_text),
            FadeOut(capacity_B_text)
            ], run_time=1, lag_ratio = 0))
        self.wait(6)
        
        # t=96
        self.play(Write(net_flow_text), run_time=2)
        self.wait(2)

        # t=100
        self.play(AnimationGroup(*[
            Transform(net_flow_text[0], capacity_flow_text[0]),
            Transform(net_flow_text[2], capacity_flow_text[2])
            ], run_time=2, lag_ratio = 0))
        self.wait(7)

        # t=109
        self.play(Transform(net_flow_text, capacity_equal_text), run_time=1)
        self.wait(20)


class FFCut(Scene):
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

        path1 = [[0,1], [1,4], [4,6]]
        path2 = [[0,2], [2,5], [5,6]]
        path3 = [[0,2], [2,3], [3,5], [5, 6]]
        path4 = [[0, 3], [3, 4], [4, 6]]
        path5 = [[0, 3], [3, 5], [5, 6]]

        FF_cut_endpoints = [[1, 4], [3, 4], [3, 5], [2, 5]]
        not_forward_full_cut_endpoints = [[1,4],[3,1],[0,3],[2,3],[2,5]]
        not_backward_full_cut_endpoints = [[1,4],[3,1],[0,3],[2,3],[2,5]]
        forward_cut_object = network.DrawCut(not_forward_full_cut_endpoints)
        backward_cut_object = network.DrawCut(not_backward_full_cut_endpoints)

        S_text = Tex("S")
        T_text = Tex("T")   
        S_text.shift(UP*2.9 + LEFT * 4.5).scale(1.5)
        T_text.shift(UP*2.9 + RIGHT * 4.5).scale(1.5)
        S_text.set_color(GREEN)
        T_text.set_color(BLUE)

        capacity_equal_text = Tex("Capacity ",r"=\ ", "Maximum flow")
        capacity_equal_text[0].set_color(YELLOW)
        capacity_equal_text.shift(UP*3.5)

        # ---------------------- Animations ----------------------

        # t=131
        self.add(VGroup(Nodes, Edges)) 
        self.wait(2)

        # Ford-Fulkerson
        # t = 133
        self.play(*network.AugmentPath(path1, amount=6), run_time=0.4)
        self.play(*network.AugmentPath(path2, amount=5), run_time=0.4)
        self.play(*network.AugmentPath(path3, amount=4), run_time=0.4)
        self.play(*network.AugmentPath(path4, amount=2), run_time=0.4)
        self.play(*network.AugmentPath(path5, amount=2), run_time=0.4)
        self.wait(5)


        # t=140
        cut_object = network.DrawCut(FF_cut_endpoints)
        self.play(AnimationGroup(*[
            Nodes[1].animate.set_color(GREEN), 
            Nodes[2].animate.set_color(GREEN),
            Nodes[3].animate.set_color(GREEN),
            Nodes[4].animate.set_color(BLUE),
            Nodes[5].animate.set_color(BLUE),
            FadeIn(S_text),
            FadeIn(T_text),
            Create(cut_object)], run_time=1, lag_ratio = 0))
        self.wait(20)

        # t=161
        self.play(Indicate(network.Edges[network.edge_endpts.index([0,1])]), run_time=1.5)
        self.wait(4.5)

        # t=166
        self.play(Indicate(Nodes[4]), run_time=1.5)
        self.wait(20.5)

        # t=188
        self.play(Transform(cut_object, forward_cut_object), run_time=1)
        self.wait(1)
        self.play(Wiggle(network.Edges[network.edge_endpts.index([0,3])]), run_time=2)
        self.wait(5)

        # t=197
        self.play(Indicate(Nodes[0]), run_time=1.5)
        self.wait(1.5)

        # t=200
        self.play(*network.AugmentPath([[0,3]], amount=1), run_time=2)
        self.wait(16)

        # t=218
        original_cut_object = network.DrawCut(FF_cut_endpoints)
        self.play(Transform(cut_object, original_cut_object), run_time=1)
        diagram = VGroup(Nodes, Edges, cut_object, S_text, T_text)
        self.play(diagram.animate.scale(0.8).shift(DOWN), run_time=1)
        self.play(Write(capacity_equal_text), run_time=2)

        self.wait(28)
        # t=250
        


