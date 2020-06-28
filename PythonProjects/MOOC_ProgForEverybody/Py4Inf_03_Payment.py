
# 3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
# Award time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use raw_input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.

normalRate = 10.5
overtimeRate = normalRate * 1.5
pay = 0
h = 0
hrs = input("Enter Hours: ")

try:
    h = float(hrs)
except:
    print("Error, please enter numeric input")
    quit()

if h <= 40:
    pay = h * normalRate
else:
    pay = 40 * normalRate + (h - 40) * overtimeRate

print(pay)
