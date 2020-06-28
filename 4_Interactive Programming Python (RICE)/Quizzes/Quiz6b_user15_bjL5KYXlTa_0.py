num = [2,3,4,5,6,7,8,9]
result = []
copyNum = []
x = 0

#while len(num)>2:
result.append(num[0])
for i in num:
    if i % result[x] !=0:
        copyNum.append(i)
num = list(copyNum)
x +=1
copyNum = []

print "result = ",result 
print "num = ",num
print "x = ", x


#-----------------------------------
print "---------------------------"
#-----------------------------------
result.append(num[0])
for i in num:
    if i % result[x] !=0:
        copyNum.append(i)
num = list(copyNum)
x +=1
copyNum = []

print "result = ",result 
print "num = ",num
print "x = ", x

#-----------------------------------
print "---------------------------"
#-----------------------------------
result.append(num[0])
for i in num:
    if i % result[x] !=0:
        copyNum.append(i)
num = list(copyNum)
x +=1
copyNum = []

print "result = ",result 
print "num = ",num
print "x = ", x

print range(2,10)

