
# 5.2 Write a program that repeatedly prompts a user for integer numbers
# until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the number.

# Enter the numbers from the book for problem 5.1 and Match the sample output below.

largest = None
smallest = None
counter = 0
while True:
    num = input("Enter a number: ")
    if num == "done": break
    if len(num) < 1: continue # check for empty line

    try:
        num = int(float(num))
    except:
        print("Invalid input")
        continue

    #print(num)
    if counter == 0:
        largest = num
        smallest = num

    if largest < num: largest = num
    if smallest > num: smallest = num

    counter += 1

print("Maximum is ", largest)
print("Minimum  is ", smallest)
