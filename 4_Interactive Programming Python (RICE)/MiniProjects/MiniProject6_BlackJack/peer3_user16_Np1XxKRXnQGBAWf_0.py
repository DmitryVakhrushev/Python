# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        hand_str = ''
        for card in self.cards:
            hand_str+=' ' + str(card)
        return "Hand contains" + hand_str

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        for card in self.cards:
            value +=  VALUES[card.get_rank()]
      
        for card in self.cards:
            if card.get_rank() == 'A':
                if value + 10 <= 21:
                    value+=10
            
            # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
            # compute the value of the hand, see Blackjack video
        return value	
   
    def draw(self, canvas, pos):
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, [pos[0] + 100*i, pos[1]])
            
               
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
                
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        card = self.deck.pop()
        return card
    
    def __str__(self):
        deck_str = ''
        for card in self.deck:
            deck_str+=' ' + str(card)
        return "Deck contains" + deck_str


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer_hand, player_hand, score, status
    
    if in_play:
        score-=1
        
    outcome = ''
    status = 'Hit or stand?'
               
    in_play = True
    
    deck = Deck()
    deck.shuffle()
    
    # dealer hand
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
        
    # player hand
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())


def hit():
    global outcome, in_play, deck, dealer_hand, player_hand, score, status
    
    if in_play:
         player_hand.add_card(deck.deal_card())
         if player_hand.get_value() > 21:
            outcome = 'You went bust and lose'
            in_play = False
            score-=1
       
def stand():
    global in_play, outcome, score, dealer_hand, player_hand, deck, status
    
    if in_play:
        
        status = 'New deal?'
        while dealer_hand.get_value() < 17:
            card = deck.deal_card()
            dealer_hand.add_card(card)
           
        if player_hand.get_value() > dealer_hand.get_value() or dealer_hand.get_value() > 21:
            outcome = 'You win!'
            score+=1
        else:
            outcome = 'You lose!'
            score-=1
            
    in_play = False
            
        
# draw handler    
def draw(canvas):
    global score, in_play, deck, player_hand, dealer_hand, outcome, status
    # test to make sure that card.draw works, replace with your code below
    player_hand.draw(canvas,[60,400])
    dealer_hand.draw(canvas,[60,200])
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [96, 249], CARD_SIZE)

    canvas.draw_text('Score  ' + str(score), (375, 100), 36, "Yellow","sans-serif")
    canvas.draw_text('Blackjack', (75, 100), 36, "Cyan","sans-serif")
    canvas.draw_text('Dealer', (60, 180), 24, "Black","sans-serif")
    canvas.draw_text(outcome, (200, 180), 24, "Black","sans-serif")
    canvas.draw_text('Player', (60, 380), 24, "Black","sans-serif")
    canvas.draw_text(status, (200, 380), 24, "Black","sans-serif")
    canvas.draw_polygon([(360, 60), (550, 60), (550, 115),(360, 115)], 5, "Brown")
    
   
   
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

 
deal()
# get things rolling
frame.start()


# remember to review the gradic rubric