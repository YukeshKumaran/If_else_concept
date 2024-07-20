#Write a Python program to check if a character is a vowel or consonant.

char=input("enter Alphabet:")
if char.lower() in ['a','e','i','o','u']:
    print("Vowel")

elif char.isalpha():
    print("consonant")
else:
    print("Invalid input ")
