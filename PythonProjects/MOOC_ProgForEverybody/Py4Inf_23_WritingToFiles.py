
#-----------------------------------------------
# Writing files
#-----------------------------------------------

# If the file already exists, opening it in write mode clears out the old data and starts fresh, so be careful!
# If the file doesn’t exist, a new one is created.
# When you are done writing, YOU HAVE TO CLOSE THE FILE
# We could close the files which we open for read as well, but we can be a little
# sloppy if we are only opening a few files since Python makes sure that all open
# files are closed when the program ends. When we are writing files, we want to
# explicitly close the files so as to leave nothing to chance.


#---------------------
# fout = open('c:/111/output.txt', 'w') # open in the file system

fout = open('output.txt', 'w') # open in the project folder

line1 = "This heres the wattle\n"
fout.write(line1)

fout.close()
#---------------------