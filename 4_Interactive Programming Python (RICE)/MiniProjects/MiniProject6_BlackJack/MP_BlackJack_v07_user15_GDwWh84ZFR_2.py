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
busted = False

plHand = ""
dealerHand = ""
plHandValue = 0
gameFinished = False


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
        return ' '.join(self.myHand) # return a string representation of a hand			
    
    def add_card(self, card):
        self.myHand.append(str(card)) # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        ace = 0
        for i in self.myHand:
            #print i[1], VALUES[i[1]]
            hand_value += VALUES[i[1]]
            if i[1] == 'A': ace += 1
        
        if ace==0:
            return hand_value
        else:
            if ace > 0 and hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value


            
    def draw(self, canvas, pos):
        #pass
        for i in self.myHand:
            i.draw(canvas,[150, 240])
            
        
        # draw a hand on the canvas, use the draw method for cards    

 
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
#define event handlers for buttons

def deal():
    global outcome, in_play, score
    global newDeck, plHand, dealerHand, gameFinished, busted
    
    
    if in_play == True and gameFinished != True:
        outcome = "You lost a point pressing Deal in the midst"
        print 
        score -= 1
        gameFinished = True
    
    else:
        gameFinished = False
                    
        newDeck = Deck()
        newDeck.shuffle()
        print "Deck = ", newDeck
        
        # Player's hand
        plHand = Hand()
        plHand.add_card(newDeck.deal_card())
        plHand.add_card(newDeck.deal_card())
        print "Player's hand = ", plHand, ", value = ", plHand.get_value()
        
        # Dealer's hand
        dealerHand = Hand()
        dealerHand.add_card(newDeck.deal_card())
        dealerHand.add_card(newDeck.deal_card())
        print "Dealer's hand = ", dealerHand, ", value = ", dealerHand.get_value()
        
        print "Deck = ", newDeck
        
        in_play = True
        busted = False
        
        outcome = "Hit or Stand?"

def hit():
    global score, busted, plHandValue, gameFinished, outcome, info
    
    if gameFinished == True:
        outcome = "Press Deal for New Game"
    
    else:
        if in_play == False:
            outcome = "Press Deal for New Game"
        else:
            # if the hand is in play, hit the player
            plHand.add_card(newDeck.deal_card())
            plHandValue = plHand.get_value()
            
            if plHandValue <= 21:
                print "Player's hand", plHand, ", value = ", plHandValue
                
            else:
                print "Player's hand", plHand, ", value = ", plHandValue
                
                busted = True
                score -= 1
                gameFinished = True
                outcome = "You have busted and lose. New Deal?"
                
                # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global busted, score, plHandValue, gameFinished, outcome
    
    if gameFinished == True:
        outcome = "Press Deal for New Game"
    
    else:
        if in_play == False:
            outcome = "Press Deal for New Game"
        
        else:
            plHandValue = plHand.get_value()
    
            if busted == True:
                outcome = "You have busted, you cannot STAND!"
            
            else:
                while dealerHand.get_value() < 17:
                    dealerHand.add_card(newDeck.deal_card())
                
                y = dealerHand.get_value()
                if y > 21:
                    score += 1
                    outcome = "Dealer lost, you win! New deal?"
        
                elif y >= plHandValue:
                    score -= 1
                    outcome = "Dealer wins :-( New Deal?"
                    
                else:
                    score += 1
                    outcome = "You win!!! New deal?"
                    
                print "-------------------------"
                print "Player's Hand = ", plHand, " value = ",plHandValue
                print "Dealer's Hand = ", dealerHand, " value = ",y
                print "-------------------------"
                
                gameFinished = True
                
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score

    
# draw handler    
def draw(canvas):

    # test to make sure that card.draw works, replace with your code below
    
    # Header and outcome
    canvas.draw_text("Blackjack", (220, 50), 40, "Magenta")
    canvas.draw_text(outcome, (100, 150), 25, "White")
    
    # Score
    canvas.draw_text("Score: " + str(score), (450, 100), 30, "White")
    
    # Dealer
    canvas.draw_text("Dealer", (50, 220), 30, "White")
    
    # Player
    canvas.draw_text("Player", (50, 440), 30, "White")
#----------------------    
    
    #plHand.draw(canvas,[150, 240])

    
    card = Card("S", "A")
    card.draw(canvas, [70, 460])
    card.draw(canvas, [70, 240])

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
#deal()


# remember to review the gradic rubric