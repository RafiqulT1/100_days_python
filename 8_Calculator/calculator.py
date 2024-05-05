# calculator
from calculator_graphics import logo
import subprocess


'''Bellow are all the finctions to do calculation based on operator'''
#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

# Dictionary of opearators
operators = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

# main logic
def calculator():

  print(logo) # Print logo of the game
  num1 = float(input("What's your first number?:")) # ask user input for first number
  # go through libary to get the operators name which can be use later in function calls
  for symbol in operators:
    print(f"[{symbol}]")
  
  should_continue = True # State of continuetion
  
  while should_continue:
    chosen_operator = input("Pick an operator from above: ") # ask user to choose an operator
    num2 = float(input("What's your next number?: ")) # ask user for second number
    calculation_function = operators[chosen_operator] 
    answer = calculation_function(num1, num2) # function call based on the chosen operator
    
    print(f"{num1} {chosen_operator} {num2} = {answer}") #prints ans
    # ask user if they wants to continue calculation using the answer or start a new calculation
    continue_calulation = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
    
    if continue_calulation == "y":
      num1 = answer
    elif continue_calulation == "n": # if the answer is "n" do a recursive funciton call to start over
      should_continue = False
      subprocess.run("clear", shell=True)
      calculator()

calculator()