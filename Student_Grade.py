def determine_grade(score):
    try:
        score = float(score)  
        if score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
        elif score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        elif score >= 70:
            print("Grade: C")
        elif score >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
    except ValueError:
        print("Invalid input. Please enter a numeric score.")

def main():
    score = input("Enter the student's score: ")
    determine_grade(score)
main()
