import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)

phonetic_dict = {row.letter:row.code for (index,row) in df.iterrows()}
# print(df_dict)

user_name = input("Please insert your name:").upper()
# alphabet_list = [alphabet for alphabet in user_name]
# print(alphabet_list)

# phonetic_words = [word for (alphabet,word) in phonetic_dict.items() if alphabet in alphabet_list]
phonetic_words = [phonetic_dict[letter] for letter in user_name]

print(phonetic_words)




#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


