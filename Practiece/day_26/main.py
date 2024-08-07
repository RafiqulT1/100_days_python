import random
import pandas
# name = "Rafiqul"
# letter_list = [letter.lower() for letter in name]
# print(letter_list)

# numb_range = range(1,5)
# num_list = [number*2 for number in numb_range]
# print(num_list)

# name_list = ["Alex", "Beth", "Cartoline", "Dave", "Elanor", "Freddie"]

# short_names = [name for name in name_list if len(name) < 5]

# long_names = [name.upper() for name in name_list if len(name) >= 5]

# print(short_names)
# print(long_names)

# -------- DICTIONARY COMPREHENSION -------------

# name_list = ["Alex", "Beth", "Cartoline", "Dave", "Elanor", "Freddie"]
# students_scores = {student:random.randint(1,100) for student in name_list}

# print(students_scores)

# passed_students = {student_name:score for (student_name, score) in students_scores.items() if score >= 50}

# print(passed_students)


# --------- LOOP THROUGH DATA FRAME -------------

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through rows of a data frame
for (index,row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

