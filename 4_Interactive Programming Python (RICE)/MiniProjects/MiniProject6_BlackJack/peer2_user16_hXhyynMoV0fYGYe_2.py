# ==============================================================    
# 					"The Blackjack Game"
# ==============================================================

# ==============================================================
import simplegui
import random
# ==============================================================

# ==============================================================
# Load the card sprite
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")
CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    
# ==============================================================

# ==============================================================
# Initialize some global variables for the game
in_play = False
outcome = "" 
score = 0
upper_message = ""
lower_message = ""
dealer_hand = []
player_hand = []
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
# ==============================================================

# ==============================================================
# Define a class named Card
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
# ==============================================================
        
# ==============================================================
# Define a class named Hand
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        currenthand = "Hand contains"
        for i in range(len(self.hand)):
            rank = self.hand[i].get_rank()
            suit = self.hand[i].get_suit()
            currenthand += " "+ suit + rank
        return currenthand

    def add_card(self, card):
        self.hand += [card]

    def get_value(self):
        value = 0
        for i in range(len(self.hand)):
            rank = self.hand[i].get_rank()
            value += VALUES[rank]
        for i in range(len(self.hand)):
            if((self.hand[i].get_rank() == 'A') and (value <= 11)):
                value += 10
        return value

    def draw(self, canvas, pos):
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas, ((i*1.25+1)*pos[0],pos[1]))
# ==============================================================    

# ==============================================================
# Define a class named Deck
class Deck:
    def __init__(self):
        self.deck = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.deck += [SUITS[i] + RANKS[j]]
                
    def shuffle(self):        
       random.shuffle(self.deck)

    def deal_card(self):
        index = random.randrange(0,len(self.deck))
        dealcard = Card(self.deck[index][0], self.deck[index][1])
        self.deck.pop(index)
        return dealcard
    
    def __str__(self):
        currentdeck = "Deck contains"
        for i in range(len(self.deck)):
            currentdeck += " "+ self.deck[i]
        return currentdeck
# ==============================================================    

# ==============================================================    
# An event handler for the Deal button
def deal():
    global outcome, in_play, dealer_hand, player_hand, upper_message, lower_message, score
    dealer_hand = Hand()
    player_hand = Hand()
    outcome = Deck()
    for i in range(0, 2):
        outcome.shuffle()
        getcard = outcome.deal_card()
        dealer_hand.add_card(getcard)
    for i in range(0, 2):
        outcome.shuffle()
        getcard = outcome.deal_card()
        player_hand.add_card(getcard)
    print "Dealer", dealer_hand
    print "Player", player_hand
    upper_message = ""
    lower_message = "Hit or stand?"
    if (in_play == True):
        score -= 1
    else:
        in_play = True
# ==============================================================    

# ==============================================================    
# An event handler for the Hit button
def hit():
    global player_hand, score, in_play, upper_message, lower_message
    if ((player_hand.get_value() <= 21) and (in_play == True)):
        getcard = outcome.deal_card()
        player_hand.add_card(getcard)
        if (player_hand.get_value() > 21):
            upper_message = "You Went Bust! You Lose!"
            lower_message = "New Deal?"
            in_play = False
            score -= 1
# ==============================================================    

# ==============================================================    
# An event handler for the Stand button
def stand():
    global dealer_hand, score, in_play, upper_message, lower_message
    if(in_play == True):
        in_play = False
        while (dealer_hand.get_value() < 17):
            getcard = outcome.deal_card()
            dealer_hand.add_card(getcard)
        if(dealer_hand.get_value() > 21):
            upper_message = "Dealer Went Bust! You Win!"
            lower_message = "New Deal?"
            score += 1
        elif (player_hand.get_value() <= dealer_hand.get_value()):
            upper_message = "You Lose!"
            lower_message = "New Deal?"
            score -= 1
        else:
            upper_message = "You Win!"
            lower_message = "New Deal?"
            score +=1
# ==============================================================    
    
# ==============================================================    
# Define a handler to draw on canvas
def draw(canvas):
    dealer_hand.draw(canvas, (75,150))
    player_hand.draw(canvas, (75,400))
    canvas.draw_text("Blackjack", (20, 50), 40, "Yellow")
    canvas.draw_text("Your Score is " + str(score), (300, 50), 40, "Yellow")
    canvas.draw_text("Dealer", (60, 135), 25, "White")
    canvas.draw_text("Player", (60, 385), 25, "White")
    canvas.draw_text(upper_message, (300, 135), 25, "White")
    canvas.draw_text(lower_message, (300, 385), 25, "White")
    if (in_play == True):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (111.5,200), CARD_BACK_SIZE)
# ==============================================================    

# ==============================================================    
deal()
# ==============================================================    

# ==============================================================    
# Create a frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")
# ==============================================================

# ==============================================================    
# Register event handlers for control elements
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
# ==============================================================

# ==============================================================    
# Start the frame
frame.start()
# ==============================================================