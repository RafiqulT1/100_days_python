from alphabet_list import alphabet
from graphics import logo


def caesar(start_text, shifting_amount, direction):
    # create variable for encode / decode text
    end_text = ""

    for char in start_text:
        if char in alphabet:
            # finds the index of the letter from alphabet list
            letter_index_position = alphabet.index(char)
            if direction == "encode":
                # shifting the letter index by user's defined shifting amount
                shifted_letter_index_position = letter_index_position + shifting_amount
                # if index gets out of range reduced by 26
                if shifted_letter_index_position > 25:
                    shifted_letter_index_position -= 26

            elif direction == "decode":
                # shifting the letter index by user's defined shifting amount
                shifted_letter_index_position = letter_index_position - shifting_amount
                # if index gets out of range increase by 26
                if shifted_letter_index_position < 0:
                    shifted_letter_index_position += 26 

            # shifts letter based on the shifted index
            shifted_letter = alphabet[shifted_letter_index_position]
            # add the shifted charec to cipher_text variable
            end_text += shifted_letter

        elif char not in alphabet:
            end_text += char

    # print the encode / decoded message  
    print(f"The {direction} text is \"{end_text}\".")



# print graphics
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
cipher_state = True

#Call the caesar function
while cipher_state:
    caesar(start_text=text, shifting_amount=shift, direction=direction)
    continue_cipher = input("Type \"yes\" if you want to go again. Otherwise type \"no\" or press enter to exit:\n").lower()

    if continue_cipher == "no" or continue_cipher == "":
        cipher_state = False
    elif continue_cipher == "yes":
        cipher_state = True


