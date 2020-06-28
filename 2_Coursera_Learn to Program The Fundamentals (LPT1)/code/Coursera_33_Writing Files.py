#-----------------------------------------
# Coursera_33_Writing Files
#-----------------------------------------

# we want to open the file and copy it into the new location
# but we also want to add a word "copy" at the very beginning of the file

# prompting a user to find a file
import tkinter.filedialog
from_filename = tkinter.filedialog.askopenfilename()

to_filename = tkinter.filedialog.asksaveasfilename()

from_file = open(from_filename,'r')
contents = from_file.read()
from_file.close()

to_file = open(to_filename,'w')
to_file.write("Copy\n")
to_file.write(contents)

to_file.close()





