#===============================================================================
# 6-1: Intro to Tkinter -- Kent D. Lee
#===============================================================================

import tkinter
import turtle
import sys


def main():
    root = tkinter.Tk() # create a window on the screen
    
    
    # creating a vidget -- an element of the GUI program
    cv = tkinter.Canvas(root, width=600, height=600) # call a Canvas constructor to create canvas
    cv.pack(side=tkinter.LEFT)
    root.title("Draw!") # changing the main window name 
    
    t = turtle.RawTurtle(cv) # create a Turtle canvas
    screen = t.getscreen()
    screen.setworldcoordinates(0,0,600,600)
    
    # Create another vidget called 'frame'
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
    
    screen.tracer(0) # to avoid stack overflow
    
    #------------------------------------------
    # Write an event handlers
    #------------------------------------------
    def quitHandler():
        print("Goodbye!")
        sys.exit(0) # exiting the program. Import 'sys' module fisrt
    
    # Create a "quit" button
    quitButton = tkinter.Button(frame, text="Quit", command=quitHandler)
    quitButton.pack()
    
    
        
    textLab = tkinter.Label(frame, text="Text to Write")
    textLab.pack()
    
    textVar = tkinter.StringVar()
    textVar.set("Hello World!")
    textEntry = tkinter.Entry(frame, textvariable = textVar)
    textEntry.pack()
    
    def writeHandler():
        t.write(textVar.get())
        
    writeButton = tkinter.Button(frame, text="Write Text", command=writeHandler)
    writeButton.pack()
    
    
    
    # On-Click method in Turlte graphics responds on the mouse clicks
    def clickHandler(x,y):
        t.goto(x, y)
        screen.update() # the program will be more responsive

    screen.onclick(clickHandler)
    
    def dragHandler(x,y):
        t.goto(x, y)
        screen.update() # the program will be more responsive

    t.ondrag(dragHandler)
    

    
    
    
    
    
    
    
    tkinter.mainloop() # it tells tkinter to start listening for events



if __name__ == '__main__':
    main()
        
        
