
# C:\Dim\Google Drive\PythonProjects\Python3EssentialTraining

print("Hello, World!")

n = 0
while True:
    n += 1
    if n > 10: break
    if n == 5 or n ==7 : continue
    print(n)


myList = ['Anna','Beatrice','Claudia','Deborah','Elise']
nums = [1,5,8,17,78,29]
count = 0
sum = 0
for i in nums:
    print(i)
    count += 1
    sum = sum + i
print("count = ", count)
print ("sum = ", sum)
print("average = ", sum/count)