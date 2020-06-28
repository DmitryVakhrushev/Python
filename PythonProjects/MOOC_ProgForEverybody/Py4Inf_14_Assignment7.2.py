
# 7.2 Write a program that prompts for a file name, then opens that file
# and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and coput the average of those values and produce an output as shown below.
# You can download the sample data
# at http://www.pythonlearn.com/code/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) == 0:
    fname = 'mbox-short.txt'
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    colonPos = line.find(":")
    toFloat = float(line[colonPos+1: ])
    total += toFloat
    count += 1
    # print(toFloat, total)
print("Average spam confidence:",total/count)
print("Done")
