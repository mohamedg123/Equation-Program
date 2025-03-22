# Equation-Program

import random

print("===Welcome To The Algebra Equation Test===")
name = input("Enter your name: ")
print(f"Welcome, {name}! Let's test your algebra skills today.\n")
print("Solve for x in each equation. You Got This! \n")

score = 0  
num_questions = 5  

def make_a_problem():
    y = random.randint(-10, 10)  # Avoid 0 to ensure solvability
    x = random.randint(-10, 10)
    a = y * x
    return (f"{y} * x = {a}", x)  # Return equation and answer

def get_user_guess(equation):
    while True:
        try:
            return int(input(f"Solve for x: {equation}\nYour answer: "))
        except ValueError:
            print("Incorrect input! Please enter a valid number.")

for i in range(num_questions):
    equation, correct_answer = make_a_problem()  
    user_answer = get_user_guess(equation)  

    if user_answer == correct_answer:
        print("Correct!\n")
        score += 1 
    else:
        print(f"Wrong! The correct answer was {correct_answer}.\n")

print(f"Test Over! You scored {score} out of {num_questions}.")
