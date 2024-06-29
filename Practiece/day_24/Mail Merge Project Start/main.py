#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# with open("/Users/rafiqul1/Desktop/100_days_python/18_/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode= "r") as letter:
#     contert = letter.read()
#     print(contert)

name_list = []
with open("./input/Names/invited_names.txt", mode="r") as name_data:
    name_data_list = name_data.readlines()

with open("./input/Letters/starting_letter.txt", mode="r") as letter_data:
    letter = letter_data.read()


for name in name_data_list:
    name_list.append(name.strip("\n"))

for name in name_list:
    with open(f"./output/ReadyToSend/LetterTo{name}.txt", mode="a") as new_letter:
        replace_name = letter.replace("[name]", name)
        new_letter.write(replace_name)



