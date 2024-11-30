import art
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
print('Welcome to Ceasar Cipher.')


# def encryption(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabets.index(letter)
#         new_pos = position + shift_amount
#         cipher_text += alphabets[new_pos]
#     print(f"The encoded text is {cipher_text}")
#
# def decryption(cipher_text, shift_amount):
#     normal_text = ""
#     for letter in cipher_text:
#         position = alphabets.index(letter)
#         new_pos = position - shift_amount
#         normal_text += alphabets[new_pos]
#     print(f"The decoded text is {normal_text}")

def ceasar(start_text, shift_amount, ceasar_direction):
    end_text = ""
    if ceasar_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift_amount
            end_text += alphabets[new_position]
        else:
            end_text += char
    print(f"The {ceasar_direction}d text is: {end_text}")


condition = True

while condition:
    direction = input("Do you want to encode or decode:\n")
    text = input("Enter your text:\n").lower()
    shift = int(input("Enter shift amount:\n"))

    if shift>26:
        shift %= 26
    # if direction == 'encode':
    #     encryption(plain_text=text, shift_amount=shift)
    # elif direction == 'decode':
    #     decryption(cipher_text=text, shift_amount=shift)
    # else:
    #     print("You can only encode and decode!")

    ceasar(start_text=text, shift_amount=shift, ceasar_direction=direction)

    resume = input("Do you want to continue (Y/N):").lower()
    if resume == 'y':
        condition = True
    else:
        condition = False
        print("Good Bye")
