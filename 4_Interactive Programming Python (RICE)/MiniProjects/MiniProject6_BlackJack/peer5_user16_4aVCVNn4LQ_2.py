# Mini-project #6 - Blackjack

import simplegui
import random

HEADER = "Blackjack"

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
        ret_string =  "Hand contains:"
        for card in self.cards:
            ret_string += "   " + str(card)
            
        return ret_string

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        has_ace = False
        card_sum = 0
        for card in self.cards:
            if card.get_rank() == "A":
                has_ace = True
            card_sum += VALUES[card.get_rank()]            
        
        if has_ace:
            if card_sum + 10 <= 21:
                return card_sum + 10
            else:
                return card_sum
        else:
            return card_sum
   
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += CARD_SIZE[1]
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        ret_string = "Deck contains"
        for card in self.cards:
            ret_string += " " + str(card)
            
        return ret_string
            
dealers_deck = Deck()
dealers_hand = Hand()
players_hand = Hand()


#define event handlers for buttons
def deal():
    global outcome, in_play, players_hand, dealers_deck, dealers_hand, score
    
    if in_play:
        outcome = "You have lost. New game. Hit or stand?"
        score -= 1
        
    dealers_deck = Deck()
    dealers_deck.shuffle()
    dealers_hand = Hand()
    players_hand = Hand()
    
    # deal two cards to dealer
    dealers_hand.add_card(dealers_deck.deal_card())
    dealers_hand.add_card(dealers_deck.deal_card())
    
    # deal two cards to player
    players_hand.add_card(dealers_deck.deal_card())
    players_hand.add_card(dealers_deck.deal_card())

    if not in_play:
        outcome = "You have " + str(players_hand.get_value()) + ". Hit or stand?"
    in_play = True
    
def hit():
    global in_play, score, players_hand, dealers_deck, dealers_hand, outcome
    # if the hand is in play, hit the player
    if in_play:
        players_hand.add_card(dealers_deck.deal_card())
        
    # if busted, assign a message to outcome, update in_play and score
    if in_play and players_hand.get_value() > 21:
        outcome = "You have busted with  " + str(players_hand.get_value()) + ". New deal?"
        in_play = False
        score -= 1
    elif in_play:
        outcome = "You have " + str(players_hand.get_value()) + ". Hit or stand?"
    
def stand():
    global in_play, score, players_hand, dealers_deck, dealers_hand, outcome
    if in_play and players_hand.get_value() > 21:
        outcome = "You have busted with " + str(players_hand.get_value()) + ". Dealer won. New deal?"
        in_play = False
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealers_hand.get_value() < 17:
            dealers_hand.add_card(dealers_deck.deal_card())

        if dealers_hand.get_value() > 21:
            outcome = "Dealer have busted with " + str(dealers_hand.get_value()) + ". New deal?"
            in_play = False
            score += 1
        elif players_hand.get_value() <= dealers_hand.get_value():
            outcome = "Dealer won with " + str(dealers_hand.get_value()) + ". New deal?"
            score -= 1
            in_play = False
        elif players_hand.get_value() > dealers_hand.get_value():
            outcome = "Player won with " + str(players_hand.get_value()) + ". New deal?"
            score += 1
            in_play = False

# draw handler
def draw(canvas):
    
    canvas.draw_text(HEADER, [255, 25], 32, "Black")
    canvas.draw_text("Score " + str(score), [255, 75], 32, "Red")
    dealers_hand.draw(canvas, [5, 125])
    
    canvas.draw_text(outcome, [5, 350], 32, "White")
    players_hand.draw(canvas, [5, 415])
    
    # if in play, cover first dealer's card
    if in_play:
        # canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [5 + CARD_CENTER[0], 125 + CARD_CENTER[1]], CARD_BACK_SIZE)



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