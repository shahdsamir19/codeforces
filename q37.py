n = int(input("enter the size of the array: "))

a = []

for i in range(0, n):

    x = input("enter next item: ")

    a.append(x)

p = int(input("enter the index of the element you want to remove: "))

a.remove(a[p])

print(a)
