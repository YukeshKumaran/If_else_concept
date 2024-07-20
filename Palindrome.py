#Write a Python program to check if a string is a palindrome or not.

char=input("Enter String:")
print("Char:",char)
if char== char[::-1]:
    print("yes It is palindrome")
else:
    print("No it is not a Palindrome")
     
