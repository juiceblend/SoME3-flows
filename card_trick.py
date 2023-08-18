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
        
      # t = 0
        S_COLOR = RED
        T_COLOR = BLUE
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
        self.wait(2)
        piles2nodes = self.transformpiles()
        # self.play(*piles2nodes, run_time=3)
        # t=7.5
        self.wait(2)
        
        
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
        
        print(adj_mat_array)
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
        
        left_capacity_text = Tex("1")
        center_capacity_text = Tex(r"$\infty$")
        right_capacity_text = Tex("1")
        left_capacity_text.shift(DOWN*2.9 + LEFT * 5.2).scale(0.8)
        center_capacity_text.shift(DOWN*3.8).scale(0.8)
        right_capacity_text.shift(DOWN*2.9 + RIGHT * 5.2).scale(0.8)

        # draw network
        
        # t=37.5
        self.play(FadeOut(self.piles_group), FadeOut(rank_nodes), run_time=0.5)
        self.play(Write(VGroup(Nodes, Edges)), run_time = 5)
        INF = int(1e9)
        graph_mat = [[int(cap) if cap != float("inf") else INF for cap in row] for row in adj_mat]
        self.wait(4)

        

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
        # t = 47
        animations_1 = network.AugmentPath(edges_visited, amount=0)
        anim_group_1 = AnimationGroup(*animations_1)
        self.play(AnimationGroup(anim_group_1, run_time=2, lag_ratio = 0.2))
        #t=49
        self.wait(14)

        #t=63
        self.play(Indicate(Nodes[0]), run_time=1)
        self.play(Write(left_capacity_text), run_time=1)
        self.wait(3)

        #t=68
        self.play(Indicate(Nodes[27]), run_time=1)
        self.play(Write(right_capacity_text), run_time=1)
        self.wait(7)

        #t=77
        self.play(Write(center_capacity_text), run_time=1)
        #t=78
        self.wait(40)
        # play other video here

        S_text = Tex("S")
        T_text = Tex("T")   
        S_text.shift(UP*3.2 + LEFT * 5.2).scale(0.8)
        T_text.shift(UP*3.2 + RIGHT * 5.2).scale(0.8)
        S_text.set_color(S_COLOR)
        T_text.set_color(T_COLOR)

        pile_1_neighbors = []
        for i in range(14, 27):
            if [1,i] in edge_endpts:
              pile_1_neighbors.append(i)
        
        highlight_1_neighbors = []
        for i in pile_1_neighbors:
            highlight_1_neighbors.append(Nodes[i].animate.set_color(S_COLOR))
            highlight_1_neighbors.append(Indicate(Edges[edge_endpts.index([1,i])]))


        #t=157
        self.play(AnimationGroup(*[Nodes[1].animate.set_color(S_COLOR),
                                   Nodes[0].animate.set_color(S_COLOR),
                             FadeIn(S_text)
                             ], run_time=1, lag_ratio = 0))
        self.wait(1)
        #t=159
        self.play(AnimationGroup(*highlight_1_neighbors, run_time=1, lag_ratio = 0))
        self.wait(4)

        k_piles = [1,2,4,9,10]
        piles_in_T = [3,5,6,7,8,11,12,13]
        pile_neighbors = []
        edge_list = []
        for j in k_piles:
          for i in range(14, 27):
              if [j,i] in edge_endpts:
                pile_neighbors.append(i)
                edge_list.append([j,i])
        
        ranks_in_T = []
        for i in range(14,27):
            if i not in pile_neighbors:
                ranks_in_T.append(i)
        
        highlight_neighbors = []
        for i in range(len(pile_neighbors)):
            highlight_neighbors.append(Nodes[pile_neighbors[i]].animate.set_color(S_COLOR))
            highlight_neighbors.append(Indicate(Edges[edge_endpts.index(edge_list[i])]))

        # t=164
        turn_k_piles_S_COLOR = [Nodes[i].animate.set_color(S_COLOR) for i in k_piles]
        self.play(AnimationGroup(*turn_k_piles_S_COLOR, run_time=1, lag_ratio = 0))
        self.wait(12)

        #t=177
        self.play(AnimationGroup(*highlight_neighbors, run_time=1, lag_ratio = 0))
        self.wait(4)

        # highlight ranks in S
        #t=183
        ranks_in_S = [Indicate(Nodes[i]) for i in pile_neighbors]
        for i in pile_neighbors:
            ranks_in_S.append(Indicate(Edges[edge_endpts.index([i,27])]))
        self.play(AnimationGroup(*ranks_in_S, 
                                 run_time=2, lag_ratio = 0))
        self.wait(3)
      
       # highlight piles in T
       #t=188
        T_pile_highlight = [Nodes[i].animate.set_color(T_COLOR) for i in piles_in_T]
        T_pile_highlight.append(Nodes[27].animate.set_color(T_COLOR))
        for i in ranks_in_T:
          T_pile_highlight.append(Nodes[i].animate.set_color(T_COLOR))
        
        for i in piles_in_T:
          T_pile_highlight.append(Indicate(Edges[edge_endpts.index([0,i])]))
        T_pile_highlight.append(FadeIn(T_text))
        self.play(AnimationGroup(*T_pile_highlight, 
                                 run_time=2, lag_ratio = 0))
        self.wait(4)
        
        #t=194
        self.play(AnimationGroup(*[Indicate(Nodes[i]) for i in k_piles], 
                                 run_time=1, lag_ratio = 0))
        self.wait(2)

        total_cut_text = Tex(r"$(13-k)$",r"$+$", r"$k'$", r"$\ge 13$")
        total_cut_text.shift(UP*3.5)
        total_cut_text[0].set_color(T_COLOR)
        total_cut_text[2].set_color(S_COLOR)

        #t=197
        anim = [Indicate(Nodes[i]) for i in piles_in_T]
        anim.append(Write(total_cut_text[0]))
        self.play(AnimationGroup(*anim, 
                                 run_time=1, lag_ratio = 0))
        self.play(Write(total_cut_text[1]),run_time=1)

        #t=200
        anim = [Indicate(Nodes[i]) for i in pile_neighbors]
        anim.append(Write(total_cut_text[2]))
        self.play(AnimationGroup(*anim, 
                                 run_time=1, lag_ratio = 0))
        self.play(Write(total_cut_text[3]))
        self.wait(22)


        #t=225
        self.play(AnimationGroup(anim_group_1, run_time=2, lag_ratio = 0.2))
        self.wait(10)





