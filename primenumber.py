#Write a Python program to check if a number is a prime number or not.
n = int(input())
if n > 1:
    for i in range(2, (n//2)+1):
        if (n % i) == 0:
            print("Not a prime number")
            break
    else:
        print("prime number")
else:
    print("Not a prime number")
 
