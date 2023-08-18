from manim import *
import numpy as np
from make_network import *

'''
File for Table of Contents, Thumbnails, etc.
'''

class TableOfContents(Scene):
    def construct(self):

        # ---------------------- Setup ----------------------

        network_image = ImageMobject("assets\\NetworkThumbnail.png")
        network_image.height = 2
        network_image.to_corner(UL)
        box1 = SurroundingRectangle(network_image, color=WHITE, buff=SMALL_BUFF)
        text1 = Tex("1. What are network flows?")
        text1.scale(0.8)
        text1.next_to(box1)
        group1 = Group(network_image, box1, text1)
        highlight1 = SurroundingRectangle(group1, color=YELLOW, buff=SMALL_BUFF)

        flow_image = ImageMobject("assets\\NetworkThumbnail.png")
        flow_image.height = 2
        flow_image.next_to(box1, DOWN)
        box2 = SurroundingRectangle(flow_image, color=WHITE, buff=SMALL_BUFF)
        text2 = Tex("2. Finding the maximum flow \\\\ through a network")
        text2.scale(0.8)
        text2.next_to(box2)
        group2 = Group(box2, flow_image, text2)
        highlight2 = SurroundingRectangle(group2, color=YELLOW, buff=SMALL_BUFF)

        card_image = ImageMobject("assets\\NetworkThumbnail.png")
        card_image.height = 2
        card_image.next_to(box2, DOWN)
        box3 = SurroundingRectangle(card_image, color=WHITE, buff=SMALL_BUFF)
        text3 = Tex("3. Card matching as a network")
        text3.scale(0.8)
        text3.next_to(box3)
        group3 = Group(box3, card_image, text3)
        highlight3 = SurroundingRectangle(group3, color=YELLOW, buff=SMALL_BUFF)

        # ---------------------- Animations ----------------------

        self.play(FadeIn(group1))
        self.wait(2)
        self.play(FadeIn(highlight1))
        self.wait(3)

        self.play(FadeIn(group2))
        self.play(Transform(highlight1, highlight2))  
        self.add(highlight2)
        self.remove(highlight1)
        self.wait(8)

        self.play(FadeIn(group3))
        self.play(Transform(highlight2, highlight3))   
        self.wait(10)


class ChapterOne(Scene):
    def construct(self):
        title = Tex("1. What is a network?").scale(1.5)
        self.play(FadeIn(title))
        self.wait(4)

class ChapterTwoPt1(Scene):
    def construct(self):
        title = Tex(r"2. Finding the maximum flow through a network",r"\\", "The Ford Fulkerson Algorithm")
        title[2].set_color(BLUE)
        self.play(Write(title[0]))
        self.play(FadeIn(title[2]))
        self.wait(4)

class ChapterTwoPt2(Scene):
    def construct(self):
        title = Tex(r"2. Finding the maximum flow through a network",r"\\", r"The Max Cut/Min Flow Algorithm")
        title[2].set_color(BLUE)
        self.play(Write(title[0]))
        self.play(FadeIn(title[2]))
        self.wait(4)

class ChapterThree(Scene):
    def construct(self):
        title = Tex("3. Card matching as a network").scale(1.5)
        self.play(FadeIn(title))
        self.wait(4)

class Conclusion(Scene):
    def construct(self):
        title = Tex("Conclusion").scale(1.5)
        self.play(FadeIn(title))
        self.wait(4)

'''
Thumbnail constructors:
Run with the -s flag to generate an image
    i.e. manim -s overview_elements.py NetworkThumbnail
'''

class TableOfContentsThumbnail(Scene):
    def construct(self):

        # ---------------------- Setup ----------------------

        network_image = ImageMobject("assets\\NetworkThumbnail.png")
        network_image.height = 2
        network_image.to_corner(UL)
        box1 = SurroundingRectangle(network_image, color=WHITE, buff=SMALL_BUFF)
        text1 = Tex("1. What are network flows?")
        text1.scale(0.8)
        text1.next_to(box1)
        group1 = Group(network_image, box1, text1)
        highlight1 = SurroundingRectangle(group1, color=YELLOW, buff=SMALL_BUFF)

        flow_image = ImageMobject("assets\\NetworkThumbnail.png")
        flow_image.height = 2
        flow_image.next_to(box1, DOWN)
        box2 = SurroundingRectangle(flow_image, color=WHITE, buff=SMALL_BUFF)
        text2 = Tex("2. Finding the maximum flow \\\\ through a network")
        text2.scale(0.8)
        text2.next_to(box2)
        group2 = Group(box2, flow_image, text2)
        highlight2 = SurroundingRectangle(group2, color=YELLOW, buff=SMALL_BUFF)

        card_image = ImageMobject("assets\\NetworkThumbnail.png")
        card_image.height = 2
        card_image.next_to(box2, DOWN)
        box3 = SurroundingRectangle(card_image, color=WHITE, buff=SMALL_BUFF)
        text3 = Tex("3. Card matching as a network")
        text3.scale(0.8)
        text3.next_to(box3)
        group3 = Group(box3, card_image, text3)
        highlight3 = SurroundingRectangle(group3, color=YELLOW, buff=SMALL_BUFF)

        # ---------------------- Animations ----------------------

        self.add(VGroup(group1,group2,group3))  
        self.wait(10)

class NetworkThumbnail(Scene):
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

        self.add(VGroup(Nodes, Edges))
        self.wait(1)
