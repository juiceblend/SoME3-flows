from manim import *
import numpy as np

class Flow(Scene):

    def MakeNodes(self, n, R, node_positions, adj_mat):
        
        Nodes = VGroup()
        Edges = VGroup()

        for i in range(n):
            node_text = Tex(str(i))
            node = Circle(radius = R, fill_color = RED, fill_opacity = 0.4).surround(node_text)
            node_gp = VGroup(node_text, node)
            node_gp.move_to(node_positions[:, i])
            
            Nodes = Nodes.add(node_gp)
        
        edge_endpts = [];

        for i in range(n):
            for j in range(n):
                if adj_mat[i,j] == 1:
                    node_i_center = Nodes[i].get_center()
                    node_j_center = Nodes[j].get_center()
                    edge = Arrow(start = node_i_center, end = node_j_center, buff = R + (np.linalg.norm(node_j_center - node_i_center)/10))
                    Edges.add(edge)
                    edge_endpts.append([i, j])

        return [Nodes, Edges, edge_endpts]
    
    def AugmentPath(self, path, edges, endpts):

        indices = [endpts.index(u) for u in path]  
        animations = [Indicate(edges[k]) for k in indices]
        
        return animations

    def construct(self):
        
        n = 7;
        r = 0.3;
        adj_mat = np.array([ [0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0]  ])
        pos = np.array([ [-5, -2.5, -2.5, 0,  2.5, 2.5, 5], [0, 3, -3, 0,  3, -3, 0], [0, 0, 0, 0, 0, 0, 0] ])
        G = self.MakeNodes(n, r, pos, adj_mat)
        Nodes = G[0]
        Edges = G[1]
        edge_endpts = G[2]

    
        self.play(Write(VGroup(Nodes, Edges)), run_time = 3)
        self.wait(1)

        path1 = [[0,1], [1,4], [4,6]]
        animations_1 = self.AugmentPath(path1, Edges, edge_endpts)
        anim_group_1 = AnimationGroup(*animations_1)
        self.play(AnimationGroup(anim_group_1, run_time=2, lag_ratio = 0.2))
