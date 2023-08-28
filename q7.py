from array import *

arr = array('i', [])

n = int(input("Enter the length of the array: "))

for i in range(n):
    y = int(input("Enter the next value: "))
    arr.append(y)

x = arr[-1::-1]

print(x)
