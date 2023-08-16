from manim import *

class Card(Square):
     
    def __init__(self, rank, suit, opacity=0.9, fill=LIGHT_GREY):
        super().__init__(fill_opacity=0.9, fill_color=LIGHT_GREY, color=suit)
        self.rank = rank
        rank_text = Text(str(rank), color=suit)
        rank_text.align_to(self.get_corner(UP+LEFT), UP+LEFT).shift(RIGHT*0.3 + DOWN*0.3)
        self.add(rank_text).scale(0.5)