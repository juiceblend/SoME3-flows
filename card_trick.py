from manim import *
from make_network import *
from Deal import *
import numpy as np
from FF import *

class Trick(Scene):
    
    def transformpiles(self):
        animations=[]
        counter = 0
        i =1
        for group in self.piles_group:
            circle = Dot(radius=0.2, fill_opacity=0.3, color=GREEN)
            circle.move_to(group.get_center())
            text = Text(str(i)).scale(0.35)
            # Position the text at the center of the dot
            text.move_to(circle.get_center())
            circle.add(text)
            animations.append(Transform(group, circle))
            i+=1
        return animations

    def construct(self):
        deal = Deal()
        deal_anims = deal.deal_cards()
        self.play(*deal_anims, run_time=2)
        self.wait(1)

        self.gpiles = [VGroup(*pile) for pile in deal.piles] #each elemet is a group representing a pile
        self.piles_group = VGroup(*self.gpiles) #all piles as a group

        self.play(self.piles_group.animate.arrange(DOWN, buff=1.8).scale(0.15), run_time=2)
        self.play(self.piles_group.animate.shift(4*LEFT), run_time=1)

        rank_nodes = VGroup()
        rank_labels = ['A','2','3','4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for i in range(13):
          n = Node(self.piles_group[i].get_center() +np.array([8, 0, 0]), label=rank_labels[i], R = 0.2, fill_color = GREEN)
          n = n.to_VGroup()
          n[0].scale(0.5)
          rank_nodes += n

        self.play(Write(rank_nodes), run_time = 1.5)
        piles2nodes = self.transformpiles()
        self.play(*piles2nodes, run_time=3)
        self.wait(1)
        
        
        source_adj_row = [0, 
                          1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0,
                          0]
        
        sink_adj_row = [0 for _ in range(28)]
        pile_adj_rows = []

        for pile in deal.piles:
            template = [0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            
            ranks = []
            for card in pile:
                ranks.append(card.rank)

            for r in range(13):
                if r in ranks:
                    template.append(float("inf"))
                else:
                    template.append(0)

            template.append(0)
            pile_adj_rows.append(template)

        adj_mat_array = [source_adj_row] + pile_adj_rows

        for _ in range(13):
            array = [0 for _ in range(27)] + [1]
            adj_mat_array += [array]

        adj_mat_array += [sink_adj_row]  
        print(adj_mat)
        adj_mat = np.array(adj_mat_array)
        inf = float("inf")
        '''adj_mat = np.array([[ 0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0,  0,  0,
   0,  0,  0,  0, inf,  0,  0, inf, inf,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,
   0, inf,  0,  0, inf,  0,  0,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
   0, inf,  0, inf,  0,  0, inf,  0, inf,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0,  0,  0,
   0,  0, inf,  0, inf,  0, inf,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0, inf,
  inf,  0,  0,  0,  0,  0, inf,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0,
   0,  0, inf,  0,  0,  0,  0, inf,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0,  0,  0,
   0, inf,  0, inf,  0,  0,  0,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0,
  inf,  0,  0,  0,  0,  0,  0, inf, inf,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf, inf,  0,  0,
  inf,  0,  0,  0,  0, inf,  0,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf, inf,  0,
   0,  0,  0,  0, inf, inf,  0,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,
   0,  0, inf,  0,  0,  0,  0,  0, inf,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, inf,  0,  0,
   0,  0,  0, inf,  0, inf, inf,  0,  0,  0,],
 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
  inf,  0,  0, inf,  0, inf,  0, inf,  0,  0,],
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
   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,]]) '''
        
        pc = [pile.get_center() for pile in self.piles_group]

        x_coords = [-6.5]
        y_coords = [0]
        for c in pc:
            x_coords.append(c[0])
            y_coords.append(c[1])
        for c in pc:
            x_coords.append(c[0] + 8)
            y_coords.append(c[1])
        x_coords.append(6.5)
        y_coords.append(0)

        pos = np.array([ x_coords, y_coords, [ 0 for _ in range(28) ] ])

        n = 28
        r = 0.2
        show_cap = True

        network = MakeNetwork(n, r, pos, adj_mat)

        Nodes = network.Nodes
        Edges = network.Edges
        edge_endpts = network.edge_endpts

        for node in Nodes:
            node[0].scale(0.5)

        # draw network
        self.play(FadeOut(self.piles_group), FadeOut(rank_nodes), run_time=0.5)

        self.play(Write(VGroup(Nodes, Edges)), run_time = 5)
        INF = int(1e9)
        graph_mat = [[int(cap) if cap != float("inf") else INF for cap in row] for row in adj_mat]

        max_flow, paths = ford_fulkerson(graph_mat, 0, 27)
        print(paths)
        print(max_flow)
        #for i in [2,1]:
        #    problem_path = paths[-i]
        #    last_path += [[25,27]]
        #    paths[-1] = last_path
        edges_visited = []
        for path in paths:
            for edge in path:
                if edge not in edges_visited and sorted(edge) not in edges_visited:
                    edges_visited.append(edge)

        # Show matching ------------------------------------------------------------------

        animations_1 = network.AugmentPath(edges_visited, amount=0)
        anim_group_1 = AnimationGroup(*animations_1)
        self.play(AnimationGroup(anim_group_1, run_time=2, lag_ratio = 0.2))
        self.wait(3)

        # Highlighted part in script -------------------------------------------------

        S_text = Tex("S")
        T_text = Tex("T")   
        S_text.shift(UP*3.2 + LEFT * 5.2).scale(0.8)
        T_text.shift(UP*3.2 + RIGHT * 5.2).scale(0.8)
        S_text.set_color(RED)
        T_text.set_color(BLUE)

        self.play(AnimationGroup(*[
            Nodes[14].animate.set_color(RED),
            Nodes[17].animate.set_color(RED),
            Nodes[20].animate.set_color(RED),
            Nodes[1].animate.set_color(BLUE),
            Nodes[4].animate.set_color(BLUE),
            Nodes[7].animate.set_color(BLUE),
            FadeIn(S_text),
            FadeIn(T_text)], run_time=1, lag_ratio = 0))
        
        self.wait(2)

        animations_1 = network.AugmentPath([[14, 27]], amount=0)
        animations_2 = network.AugmentPath([[17, 27]], amount = 0)
        animations_3 = network.AugmentPath([[20, 27]], amount = 0)
        self.play(*animations_1, *animations_2, *animations_3, run_time = 2)
        self.wait(3)

        animations_4 = network.AugmentPath([[0, 1]], amount=0)
        animations_5 = network.AugmentPath([[0, 4]], amount = 0)
        animations_6 = network.AugmentPath([[0, 7]], amount = 0)
        self.play(*animations_4, *animations_5, *animations_6, run_time = 2)
        self.wait(3)







