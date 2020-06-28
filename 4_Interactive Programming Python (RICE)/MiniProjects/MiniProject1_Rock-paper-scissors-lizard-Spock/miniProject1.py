
#-------------------------------------------------
# Mini Project #1
# Rock-paper-scissors-lizard-Spock template
#-------------------------------------------------

# Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors
# that allows five choices. Each choice wins against two other choices,
# loses against two other choices and ties against itself. 

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers as follows:
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

#-------------------------------------------------
import sys
import random 

def rpsls(name):
    
     # convert name to player_number using name_to_number
     playerNumber = (name_to_number(name))
     print('Player chooses '+ name)
    
     # compute random guess for comp_number using random.randrange() 
     # convert comp_number to name using number_to_name
     compNumber = random.randint(0, 4)
     print('Computer chooses '+ number_to_name(compNumber))
          
     # compute difference of player_number and comp_number modulo five
     diff = (playerNumber - compNumber)%5
     
     # use if/elif/else to determine winner
     if diff == 0:
         print("Player and computer tie!")
     
     elif (diff > 0) and (diff < 3):
         print("Player wins!")
    
     else:
         print("Computer wins!")
     
     print('') # adding a line between games

#-------------------------------------------------
# helper functions "number_to_name" and "name_to_number"
#-------------------------------------------------

def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
 
    if number == 0:
        winame = 'rock'
     
    elif number == 1:
        winame = 'Spock'
     
    elif number == 2:
        winame = 'paper'
     
    elif number == 3:
        winame = 'lizard'
     
    elif number == 4:
        winame = 'scissors'
         
    return winame

#-------------------------------------------------
def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    
    nameList = ['rock','Spock','paper','lizard','scissors']
    if name not in (nameList):
        sys.exit("Please choose among rock, Spock, paper, lizard, or scissors")

    if name == 'rock':
        mynum = 0
    
    elif name == 'Spock':
        mynum = 1
    
    elif name == 'paper':
        mynum = 2
    
    elif name == 'lizard':
        mynum = 3
    
    elif name == 'scissors':
        mynum = 4
    
    return mynum

   
#-------------------------------------------------
# test your code
#-------------------------------------------------
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


