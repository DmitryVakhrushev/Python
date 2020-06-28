#---------------------------------
# Mini-project #6 - Blackjack
#---------------------------------

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

#-------------------
# my Variables
newDeck = []

#-------------------
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

#-----------------------
# define hand class
class Hand:
    def __init__(self):
        self.myHand = [] # create Hand object

    def __str__(self):
        #return "Hand contains " + str(self.myHand)
        #return "Hand contains " + ' '.join(self.myHand) # return a string representation of a hand
        return ' '.join(self.myHand) # return a string representation of a hand			
    
    def add_card(self, card):
        self.myHand.append(str(card)) # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        pass	# compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards    

 
#-----------------------       
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                self.deck.append(str(i) + str(j))
                
    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.deck)

    def deal_card(self):
        x = self.deck.pop(0)
        return Card(x[0],x[1])# deal a card object from the deck
    
    def __str__(self):
        return ' '.join(self.deck)


#---------------------



plHand = ""
dealerHand = ""
    
#define event handlers for buttons
def deal():
    global outcome, in_play
    global newDeck, plHand, dealerHand

    # your code goes here
    newDeck = Deck()
    newDeck.shuffle()
    print newDeck
    
    plHand = Hand()
    plHand.add_card(newDeck.deal_card())
    plHand.add_card(newDeck.deal_card())
    print "player hand = ", plHand
    #print newDeck
    
    dealerHand = Hand()
    dealerHand.add_card(newDeck.deal_card())
    dealerHand.add_card(newDeck.deal_card())
    print "dealer hand = ", dealerHand
    print newDeck
    
    
    
    
    in_play = True

def hit():
    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# remember to review the gradic rubric