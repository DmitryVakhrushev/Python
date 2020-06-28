
# Excercise 3.3

#3.3 Write a program to prompt the user for a score using raw_input.
# Print out a letter grade based on the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit.
# For the test, enter a score of 0.85.

sc = input("Enter your score: ")
try:
    score = float(sc)
except:
    score = -1

if score >= 0 and score <= 1:
    if score >= 0.9:
        print(score, " A")
    elif score >=0.8:
        print(score, " B")
    elif score >=0.7:
        print(score, " C")
    elif score >=0.6:
        print(score, " D")
    else:
        print(score, " F")
else:
    print("Input correct score value")
