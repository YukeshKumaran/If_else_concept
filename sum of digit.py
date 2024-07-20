def sum_of_digits(number):
    try:
        number = abs(int(number))  
        sum_digits = sum(int(digit) for digit in str(number))
        print(f"Sum of digits: {sum_digits}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
def main():
    number = input("Enter a number to calculate the sum of its digits: ")
    sum_of_digits(number)
main()
