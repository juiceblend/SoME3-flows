from manim import *
from make_network import *
from Deal import *
import numpy as np

class Trick(Scene):
    
    def transformpiles(self):
        animations=[]
        for group in self.piles_group:
            circle = Dot(radius=0.2, fill_opacity=0.9, color=GREEN)
            circle.move_to(group.get_center())
            animations.append(Transform(group, circle))
        return animations

    def construct(self):
        deal = Deal()
        deal_anims = deal.deal_cards()
        self.play(*deal_anims, run_time=2)
        self.wait(1)

        self.gpiles = [VGroup(*pile) for pile in deal.piles] #each elemet is a group representing a pile
        self.piles_group = VGroup(*self.gpiles) #all piles as a group

        self.play(self.piles_group.animate.arrange(DOWN, buff=1.2).scale(0.15), run_time=2)

        piles2nodes = self.transformpiles()
        self.play(*piles2nodes, run_time=3)
        
        
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

            for r in range(0,13):
                if r in ranks:
                    template.append(np.inf)
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

        pc = [pile.get_center() for pile in self.piles_group]

        x_coords = [-6]
        y_coords = [0]
        for c in pc:
            x_coords.append(c[0] - 4)
            y_coords.append(c[1])
        for c in pc:
            x_coords.append(c[0] + 4)
            y_coords.append(c[1])
        x_coords.append(6)
        y_coords.append(0)

        pos = np.array([ x_coords, y_coords, [ 0 for _ in range(28) ] ])

        n = 28
        r = 0.2
        show_cap = True

        network = MakeNetwork(n, r, pos, adj_mat)

        Nodes = network.Nodes
        Edges = network.Edges
        edge_endpts = network.edge_endpts

        # draw network
        self.play(FadeOut(self.piles_group), run_time=0.5)

        self.play(Write(VGroup(Nodes, Edges)), run_time = 5)
        self.wait()