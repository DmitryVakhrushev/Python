
#==============================================================================
# Lesson #38: Operating on bitwise values
#==============================================================================#

def b(n):
    '''
    The function converts a number to a binary interpretation
    '''
    print('{:08b}'.format(n))

b(5) # 00000101

x = 85 # 0x55 # 01010101
y = 51 # 0x33 # 00110011

b(x) # 01010101
b(y) # 00110011

#--------------------------------------
# Binary Operations

# OR
b(x | y) # 01110111

# AND
b(x & y) # 00010001

# XOR (0 = 0+0 OR 1+1)
b(x ^ y) # 01100110

b(x ^ 0)#01010101
b(x ^ 0xff) # 0xff = 255 # 10101010 --> flips ALL bits

# Shifting bits
print(x)
b(x << 4) # 10101010000 --> clears all the bits on the RIGHT
b(x >> 4) # 00000101 --> clears ALL the bits on the LEFT
b(~x) # -1010110 -->
