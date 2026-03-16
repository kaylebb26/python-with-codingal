import math

def calculate_square_root(number):
    """Calculate the square root of a number."""
    if number < 0:
        return "Error: Cannot calculate square root of negative number"
    return math.sqrt(number)

# Example usage
num = float(input("Enter a number: "))
result = calculate_square_root(num)
print(f"Square root of {num} is {result}")