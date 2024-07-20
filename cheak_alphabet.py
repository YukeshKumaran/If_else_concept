def is_alphabet(char):
    if char.isalpha():
        print(f"'{char}' is an alphabet character.")
    else:
        print(f"'{char}' is not an alphabet character.")

def main():
    char = input("Enter a character to check if it is an alphabet: ")
    if len(char) != 1:
        print("Please enter a single character.")
    else:
        is_alphabet(char)
main()
