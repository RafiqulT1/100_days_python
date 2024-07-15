#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= random.randint(6, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


password_list = []

for letter in range(0, nr_letters):
  password_list.append(random.choice(letters))
  
for symbol in range(0, nr_symbols):
  password_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
  password_list.append(random.choice(numbers))


random.shuffle(password_list)
random_password = ""

for charecter in password_list:
  random_password += charecter

print(f"AI generated new random password for you: {random_password}")
