x = input("please enter a text: ")
reverse = x[::-1]
print(reverse)

if x == reverse:
    print("The text is palindrome")
else:
    print("The text is not palindrome")
