year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap Year")
        else:
            print("Not leap Year")
    else:
        print("leap Year")
else:
    print("Not leap Year")
