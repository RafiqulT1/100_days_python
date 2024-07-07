# name = "Rafiqul"
# letter_list = [letter.lower() for letter in name]
# print(letter_list)

# numb_range = range(1,5)
# num_list = [number*2 for number in numb_range]
# print(num_list)

name_list = ["Alex", "Beth", "Cartoline", "Dave", "Elanor", "Freddie"]

short_names = [name
               for name in name_list
               if len(name) < 5]

long_names = [name.upper() for name in name_list if len(name) >= 5]

print(short_names)
print(long_names)