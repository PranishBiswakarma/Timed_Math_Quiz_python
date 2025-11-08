import random 
import time 


OPERATORS = ["+", "-", "*",]
MIN_OPERANDS = 3
MAX_OPERANDS = 12
TOTAL_QUESTIONS = 5


def generate_expression():
    left = random.randint(MIN_OPERANDS, MAX_OPERANDS)
    right = random.randint(MIN_OPERANDS, MAX_OPERANDS)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press Enter to start the quiz...")
print("--------------------------------")

start_time = time.time()

for i in range(TOTAL_QUESTIONS):
    expr, answer = generate_expression()
    while True:
      guess = input("Question #" + str(i+1) + ": " + expr + " = ")
      if guess == str(answer):
          print("Correct!")
          break
      wrong += 1

end_time = time.time()
total_time = end_time - start_time
      
print("--------------------------------")
print("Quiz Over! You got " + str(TOTAL_QUESTIONS - wrong) + " out of " + str(TOTAL_QUESTIONS) + " correct in " + str(int(total_time)) + " seconds.")