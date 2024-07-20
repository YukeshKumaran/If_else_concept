def find_duplicate_number(nums):
    observed = set()
    for number in nums:
        if number in observed:
            return number
        observed.add(number)
    return None

def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    duplicate_number = find_duplicate_number(nums)
    if duplicate_number is not None:
        print(f"Duplicate number found: {duplicate_number}")
    else:
        print("No duplicate number found.")
 main()
