string = input("please enter a text: ")

digit = letter = 0

for i in string:

    if i.isdigit():

        digit += 1

    elif i.isalpha():

        letter += 1

    else:

        pass

print("letters = "+str(letter))

print("digits = "+str(digit))
