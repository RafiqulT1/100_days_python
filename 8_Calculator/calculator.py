# calculator
from calculator_graphics import logo
import subprocess

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


operators = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's your first number?:"))
  for symbol in operators:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    chosen_operator = input("Pick an opeator: ")
    num2 = float(input("What's your next number?: "))
    calculation_function = operators[chosen_operator]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {chosen_operator} {num2} = {answer}")
    continue_calulation = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
    
    if continue_calulation == "y":
      num1 = answer
    elif continue_calulation == "n":
      should_continue = False
      subprocess.run("clear", shell=True)
      calculator()

calculator()