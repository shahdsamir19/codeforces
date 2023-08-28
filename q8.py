n = int(input("enter number of elements: "))
l = []

for i in range(0, n):
    x = input("Enter next value: ")
    l.append(x)

target = int(input("Enter the position of the element you want to erase: "))

l.remove(l[target-1])
print(l)