string = input("please enter a text: ")

n = int(input("enter the index of the character you want to remove: "))

if n < len(string):

    new_string = string[:n-1]+string[n:]

    print(new_string)
else:
    print("index not found")