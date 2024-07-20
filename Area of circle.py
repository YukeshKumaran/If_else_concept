import math
def calculate_area_of_circle(radius):
    try:
        radius = float(radius)
        if radius < 0:
            print("Radius cannot be negative.")
        else:
            area = math.pi * (radius ** 2)  
            print(f"Area of the circle: {area:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the radius.")

def main():
    radius = input("Enter the radius of the circle: ")
    calculate_area_of_circle(radius)

main()
