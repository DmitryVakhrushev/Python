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
msg_player = "Hit or stand?"
score = 0
wait4stand = True

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
        # create Hand object
        self.hand = []
        
    def __str__(self):
        # return a string representation of a hand        
        ret = ""        
        for i in self.hand:
            ret += i.__str__() + " "
        return "Hand contains " + ret 
        
    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        
        # Calculate hand_value
        hand_value = 0
        ace = 0 # Number of aces
        for i in self.hand:
            if VALUES[i.get_rank()] == 1:
                ace += 1
            hand_value += VALUES[i.get_rank()]
            
        # Check if hand has one Ace
        if ace == 0:
            return hand_value
        elif hand_value + 10 <= 21:
            return hand_value + 10
        else:
            return hand_value
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.myInit()
        
    def shuffle(self):
        # add cards back to deck and shuffle
        # use random.shuffle() to shuffle the deck        
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        ret = ""
        for i in self.deck:
            ret += i.__str__() + " "
        return "Deck contains " + ret 
    
    def myInit(self):
        self.deck = [];
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank)) 
                
#define event handlers for buttons
def deal():
    global outcome, in_play, wait4stand, msg_player
    
    #  shuffles the deck and deals the two cards to both the dealer and the player
    global dealer_hand, player_hand, deck
    
    wait4stand = True    
    dealer_hand = Hand() 
    player_hand = Hand()

    deck = Deck()
    
    print deck
    deck.shuffle()
    print deck
    
    for i in range (0,2):
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
    print "dealer_hand"
    print dealer_hand
    print "player_hand"
    print player_hand
    print "PLAYER " + str(player_hand.get_value())
    
    in_play = True
    outcome = ""
    msg_player = "Hit or stand?"
    
def hit():	
    global score, in_play, outcome, msg_player     
    
    # if the hand is in play, hit the player
    if in_play == True:       
        player_hand.add_card(deck.deal_card())        
        print "PLAYER " + str(player_hand.get_value())
    
    # if busted, assign a message to outcome, update in_play and score
    if player_hand.get_value() > 21:
        outcome = "You went bust and lose"
        score -= 1
        msg_player = "New deal?"
        print outcome
        in_play = False       
    
def stand():  
    global in_play, score, outcome, wait4stand, msg_player
    
    wait4stand = False # Dealer's first set visible
    
    if player_hand.get_value() > 21:
        outcome =  "You went bust and lose"    
        score -= 1
        label.set_text("Score = " + str(score))
        msg_player = "New deal?"
        print outcome 
        return
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True:        
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())            
            print "DEALER " + str(dealer_hand.get_value())    
            
        # assign a message to outcome, update in_play and score
        in_play = False
        msg_player = "New deal?"
        if (player_hand.get_value() > dealer_hand.get_value()) or (dealer_hand.get_value() > 21):        
            outcome = "You win"    
            score += 1
        else:
            outcome = "You lose"    
            score -= 1       
    print outcome
        
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    global dealer_hand, player_hand, score, wait4stand, outcome
    
    canvas.draw_text("BLACKJACK", (100, 120), 38, "Red")
    canvas.draw_text("score: " + str(score), (400, 120), 38, "Black")

    canvas.draw_text("Dealer ", (100, 180), 38, "Black")
    canvas.draw_text(outcome, (250, 180), 38, "Black")
    canvas.draw_text("Player ", (100, 340), 38, "Black")
    canvas.draw_text(msg_player, (250, 340), 38, "Black")    
    
    # Draw dealer's hand
    pos = [150, 200]
    i = 0
    for card in dealer_hand.hand:
        card.draw(canvas, [pos[0]+i*CARD_SIZE[0], pos[1]])
        i += 1

    if wait4stand == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (150+CARD_SIZE[0]/2,200+CARD_SIZE[1]/2), CARD_SIZE)
        
    # Draw player's hand
    pos = [150, 400]
    i = 0
    for card in player_hand.hand:
        card.draw(canvas, [pos[0]+i*CARD_SIZE[0], pos[1]])
        i += 1   
    
deal()

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