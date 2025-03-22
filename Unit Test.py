import random

print("Welcome to the Simple Algebra Equation Test")
print("Solve for x in each equation\n")

score = 0
num_questions = 5  

def simple_equation():
    y = random.randint(-10, 10)
    x = random.randint(-10, 10)  # Keep x random without passing it
    a = y * x
    return (f"{y} * x = {a}", x)  # Return both the equation and the correct answer

# Example usage:
equation, answer = simple_equation()
print(equation)  # Display the equation
print("Correct Answer (for testing):", answer)  # Show correct answer for debugging
