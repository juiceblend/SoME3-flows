from manim import *
from Deck import *

class Deal(Scene):
    
    def deal_cards(self):
        deck_obj = Deck()
        deck = deck_obj.cards

        # Two rows for the piles, with more spacing
        locations = [(i*2 - 6 + j)*RIGHT + (j-3+2*j)*DOWN for j in range(2) for i in range(7 if j == 0 else 6)]

        self.piles = [[] for _ in range(13)]
        animations = []
        for i in range(52):
            # Add each card to a pile
            pile_number = i // 4
            self.piles[pile_number].append(deck[i])

            # Move the card to the correct pile, offset slightly upwards based on the pile's current length
            animations.append(deck[i].animate.move_to(locations[pile_number] - UP*len(self.piles[pile_number])*0.4))
        return animations
    
    def construct(self):
        self.play(*self.deal_cards(), run_time=0.3)
