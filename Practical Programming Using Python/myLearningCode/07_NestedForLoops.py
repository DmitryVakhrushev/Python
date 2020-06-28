
#===============================================================================
# 07_Nested For Loops.py -- Kent D. Lee
#===============================================================================

print("      ",end="")

for i in range(16):
    print("%5d|" %i, end='')
    
print()
print("------"*17)

for i in range(16):
    print("%5d|" %i,end="")
    
    for j in range(16):
        print("%5d|" %(i*j),end="")
        
    print()

