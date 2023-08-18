from manim import *

class Card(Square):
     
    def __init__(self, rank, suit, opacity=0.9, fill=LIGHT_GREY):
        super().__init__(fill_opacity=0.9, fill_color=LIGHT_GREY, color=suit)
        self.rank = rank
        rank_to_text = rank +1
        if rank_to_text == 1:
            rank_to_text = 'A'
        elif rank_to_text == 11:
            rank_to_text = 'J'
        elif rank_to_text == 12:
            rank_to_text = 'Q'
        elif rank_to_text == 11:
            rank_to_text = 'K'
        self.rank_label = rank_to_text
        rank_text = Text(str(rank_to_text), color=suit)
        rank_text.align_to(self.get_corner(UP+LEFT), UP+LEFT).shift(RIGHT*0.3 + DOWN*0.3)
        self.add(rank_text).scale(0.5)