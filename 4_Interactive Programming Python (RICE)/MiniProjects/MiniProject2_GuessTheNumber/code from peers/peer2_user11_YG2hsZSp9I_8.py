import simplegui, random, math
# initialize global variables used in your code

def reset_game(max):
    """Start Game and Initialize Variables"""
    global guess_count, secret_number, high
    guess_count = 0
    high = max
    secret_number = random.randrange(0,high)
    print "New game started in the range of 0 to " + str(high)
    #print "The secret number is: " + str(secret_number) + "  The high is: " + str(high)

# define event handlers for control panel
    
def range100():
    """button that changes range to range [0,100) and restarts"""
    reset_game(100)

def range1000():
    """button that changes range to range [0,1000) and restarts"""
    reset_game(1000)
    
def get_input(guess):
    """main game logic goes here"""
    global guess_count
    guess = int(guess)
    if 2 ** guess_count <= high + 1:
        if guess > 0 and guess < high:
            guess_count += 1
            num_guesses_left = int(math.log(high, 2) +1 - guess_count)
            print "Your guess was: " + str(guess)
            if guess == secret_number:
                print "Correct! You took " + str(guess_count) + " tries."
            elif guess > secret_number:
                    print "Lower .... " + str(num_guesses_left) + " guesses remaining"
            else:
                print "Higher .... " + str(num_guesses_left) + " guesses remaining"
        else:
            print "Pick something in the range of 0 to " + str(high)
            print
        print
    else:
        print "You Lost! Starting a new game."
        print
        reset_game(high)

        
# create frame
gtn_frame = simplegui.create_frame("Guess The Number!", 200,200)

# register event handlers for control elements
btn_100 = gtn_frame.add_button("100",range100,75)
btn_1000 = gtn_frame.add_button("1000",range1000,75)
gtn_frame.add_input("Enter guess!",get_input,75)
# start frame
gtn_frame.start()

# always remember to check your completed program against the grading rubric
reset_game(100)