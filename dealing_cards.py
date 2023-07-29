from manim import *
import random

class Card(Scene):
    def construct(self):
        colors = [PURPLE, RED, DARK_BLUE, GREEN_E]
        # A deck of 52 squares (cards) with their indices (rank) written on them
        deck = []
        for i in range(52):
            square = Square(fill_opacity=0.9, fill_color=LIGHT_GREY, color=colors[i // 13])
            text = Text(str(i % 13), color=colors[i // 13])
            text.align_to(square.get_corner(UP+LEFT), UP+LEFT).shift(RIGHT*0.3 + DOWN*0.3)
            deck.append(square.add(text).scale(0.5))

        # 13 empty piles
        piles = [[] for _ in range(13)]

        # Two rows for the piles, with more spacing
        locations = [(i*2 - 6 + j)*RIGHT + (j-3+2*j)*DOWN for j in range(2) for i in range(7 if j == 0 else 6)]

        # Shuffle the deck
        random.shuffle(deck)

        for i in range(52):
            # Add each card to a pile
            pile_number = i // 4
            piles[pile_number].append(deck[i])

            # Move the card to the correct pile, offset slightly upwards based on the pile's current length
            self.play(deck[i].animate.move_to(locations[pile_number] - UP*len(piles[pile_number])*0.4), run_time=0.5)

        self.wait()
