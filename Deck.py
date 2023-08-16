from manim import *
import random
from Card import *

class Deck:
    
    def __init__(self, suit_colors=[PURPLE, RED, DARK_BLUE, GREEN_E]):
        
        # A deck of 52 squares (cards) with their indices (rank) written on them
        self.cards = []
        for i in range(52):
            card = Card(i % 13, suit_colors[i // 13])
            self.cards.append(card)

        random.shuffle(self.cards)