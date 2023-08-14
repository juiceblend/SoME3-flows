from manim import *
import numpy as np
from make_network import *

class Intro(Scene):
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

        labels = ["Paris", "Calais", "Ghent", "Brussels", "Antwerp", "Rotterdam", "Amsterdam"]
        
        network = MakeNetwork(n, r, pos, adj_mat, show_capacity=False, labels=labels, highlight_endpoints = True)
        Nodes = network.Nodes
        Edges = network.Edges
        cities = VGroup(Nodes[0], Nodes[n-1])

        # ---------------------- Animations ----------------------

        # Script:
        # Let's imagine we have two cities connected by some railway system.

        self.wait(1)

        self.play(Write(cities), run_time = 1)

        self.wait(4)

        # Script:
        # In this middle there might be some stops

        self.play(Write(Nodes[1:n-1]), run_time = 1)
        self.wait(2)

        # With trains running to and from those stops.

        self.play(Write(Edges), run_time = 2)
        self.wait(2)

        # Each train has some capacity; some maximum number of passengers it can hold.
        capacity_network = MakeNetwork(n, r, pos, adj_mat, show_capacity=True, labels=labels, highlight_endpoints = True)
        edge_transform, vertex_transform = Transform(Edges, capacity_network.Edges), Transform(Nodes, capacity_network.Nodes)
        self.play(AnimationGroup(edge_transform, vertex_transform, run_time=1, lag_ratio=0))
        self.wait(18)

        
class Path_Flow(Scene):
    def construct(self):

        # ---------------------- Setup ----------------------

        Paris = Node([-5,0,0], 'Paris', fill_color=GREEN)
        Amsterdam = Node([5,0,0], 'Amsterdam', fill_color=GREEN)
        Calais = Node([-2.5, 3, 0], 'Calais')
        Antwerp = Node([2.5, 3, 0], 'Antwerp')
        Ghent = Node([-2.5, -3, 0], 'Ghent')
        Brussels = Node([0,0,0], 'Brussels')
        Rotterdam = Node([2.5, -3, 0], 'Rotterdam')

        train1 = Edge(Paris, Calais, 8, display_capacity = True)
        train2 = Edge(Calais, Antwerp, 6, display_capacity = True)
        train3 = Edge(Antwerp, Amsterdam, 11, display_capacity = True)

        other_trains = [Edge(Paris, Brussels, 5, display_capacity = True),
                        Edge(Paris, Ghent, 9, display_capacity = True),
                        Edge(Ghent, Brussels, 7, display_capacity = True),
                        Edge(Ghent, Rotterdam, 5, display_capacity = True),
                        Edge(Rotterdam, Amsterdam, 13, display_capacity = True),
                        Edge(Rotterdam, Antwerp, 4, display_capacity = True),
                        Edge(Brussels, Antwerp, 2, display_capacity = True),
                        Edge(Brussels, Calais, 1, display_capacity = True),
                        Edge(Brussels, Rotterdam, 6, display_capacity = True)]

        route = Network([Paris, Calais, Antwerp, Amsterdam], [train1, train2, train3])
        route_cities, route_trains = route.to_VGroup()
        route_object = VGroup(route_cities, route_trains)

        everything_else = Network([Ghent, Brussels, Rotterdam], other_trains)
        else_cities, else_trains = everything_else.to_VGroup()
        else_object = VGroup(else_cities, else_trains)

        max_along_path_text = Tex("Maximum capacity along route $= 6$")
        max_along_path_text.shift(3*UP)

        max_flow_text = Tex("What is the maximum capacity through the entire network?")
        max_flow_text.shift(3*UP)

        # ---------------------- Animations ----------------------

        route_object.generate_target()
        route_object.target.shift(3*DOWN)

        self.add(route_object)
        self.add(else_object)
        self.wait(1)

        self.play(Indicate(route_trains), run_time=3)

        self.play(AnimationGroup(*[FadeOut(else_object), MoveToTarget(route_object)], run_time=2, lag_ratio = 0.3))

        self.play(FadeIn(max_along_path_text))
        self.wait(16)
        self.play(FadeOut(max_along_path_text))

        route_object.target.shift(2*UP).scale(0.7)
        else_object.shift(0.35*DOWN).scale(0.7)
        self.play(AnimationGroup(*[MoveToTarget(route_object), FadeIn(else_object)], run_time=2, lag_ratio = 0.3))
        self.wait(2)

        self.play(FadeIn(max_flow_text))
        self.wait(25)

        





        

