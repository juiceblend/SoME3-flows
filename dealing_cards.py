from manim import *
from Deck import *

class Deal(Scene):
    
    def construct(self):

        deck_obj = Deck()
        deck = deck_obj.cards
        # 13 empty piles
        piles = [[] for _ in range(13)]

        # Two rows for the piles, with more spacing
        locations = [(i*2 - 6 + j)*RIGHT + (j-3+2*j)*DOWN for j in range(2) for i in range(7 if j == 0 else 6)]

        for i in range(52):
            # Add each card to a pile
            pile_number = i // 4
            piles[pile_number].append(deck[i])

            # Move the card to the correct pile, offset slightly upwards based on the pile's current length
            self.play(deck[i].animate.move_to(locations[pile_number] - UP*len(piles[pile_number])*0.4), run_time=0.5)

        self.wait()
