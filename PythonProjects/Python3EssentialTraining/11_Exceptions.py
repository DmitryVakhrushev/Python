
# Handling errors with exceptions

try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)

except IOError as e:
    print("Doesn't work ({}))".format(e))

print("the next step")


# except:
#     print("Doesn't work")
