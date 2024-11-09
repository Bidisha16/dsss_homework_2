
import random

def gen_random_num(min, max):
    """
    Generates a random integer within the given range.
    Args:
        min (int): The minimum value of the range.
        max (int): The maximum value of the range.
    Returns:
        int: A random integer between min and max.
    """
    return random.randint(min, max)

def select_random_op():
    """
    Selects a random operator from '+', '-', and '*'.

    Returns:
        str: A randomly chosen operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])

def calc_problem(n1, n2, op):
    """
    Generates a math problem string and calculates the answer.
    Args:
        n1 (int): The first operand in the problem.
        n2 (int): The second operand in the problem.
        op (str): The operator for the math problem.
    Returns:
        tuple: A tuple containing the problem as a string and the correct answer as an int.
    """
    problem = f"{n1} {op} {n2}"
    # Calculate the answer based on the operator op
    if op == '+': 
        answer = n1 + n2
    elif op == '-': 
        answer = n1 - n2
    else: 
        answer = n1 * n2
    return problem, answer

def math_quiz():
    """
    Runs a math quiz game where the user is prompted to answer math problems generated randomly.
    Keeps track of their score and displays the total score in the end.
    """
    score = 0
    total_questions = 3
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    for _ in range(total_questions):
        # Generate random numbers n1 and n2
        n1 = gen_random_num(1, 10)
        n2 = gen_random_num(1, 5)
        # Generate an operator for the question
        op = select_random_op()
        # Generate the problem and the correct answer
        problem, correct_ans = calc_problem(n1, n2, op)
        print(f"\nQuestion: {problem}")        
        # Get the user input and check if it is valid
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        # Check if the answer given by the user is correct
        if user_answer == correct_ans:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_ans}.")
    # Prints the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")
if __name__ == "__main__":
    math_quiz()
