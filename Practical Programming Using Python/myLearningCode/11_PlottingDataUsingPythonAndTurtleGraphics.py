#===============================================================================
# 4-2: Plotting Data using Python and Turtle Graphics 
#===============================================================================

import turtle
import datetime

# Opent the file for reading
#file = open('C:\\Dim\\Google Drive\\Python\\Practical Programming Using Python\\djia.txt','r')

file = open('C:\\Dim\\Google Drive\\Python\\Practical Programming Using Python\\djia3col.csv','r')


# initialize variables
maxDJIA = 0
startDate = datetime.datetime(1900, 1, 1)
maxDate = startDate

for line in file:
    lst = line.split(',')
     
    dateStr = lst[0]
#     djia = float(lst[1])
    
    djia = (lst[1])
    
    com = lst[2]
     
#     year = int(dateStr[0:2]) + 1900
#     month = int(dateStr[2:4])
#     day = int(dateStr[4:6])
#      
#     date = datetime.datetime(year, month, day)
#       
#     if djia > maxDJIA:
#         maxDJIA = djia
#          
#     if date > maxDate:
#         date = maxDate
        
    
#     print (lst)
    print(lst[0],lst[1],lst[2])

#     
# dateDiff = maxdate - startDate
# totalDays = dateDiff.days # method
# 
# t = turtle.Turtle()
# screen = t.getscreen()
# 
# screen.setworldcoordinates(0, 0, totalDays, maxDJIA)
# 
# t.goto(0,0)


file.close()





 