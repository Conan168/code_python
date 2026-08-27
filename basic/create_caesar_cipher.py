alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'Q', 'R', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print ("Welcome to caesar cipher")

# def encrypt(original_message, shift_amount):
#     encrypt_message = ""

#     for letter in original_message:
#         encrypt_position = alphabet.index(letter) + shift_amount

#         if encrypt_position > len(alphabet) - 1:
#             encrypt_position = encrypt_position - len(alphabet)
#             encrypt_message += alphabet[encrypt_position]
#         else:
#             encrypt_message += alphabet[encrypt_position]

#     print(f"encrypt message is: {encrypt_message}")

# def decrypt(original_message, shift_amount):
#     decrypt_message = ""

#     for letter in original_message:
#         decrypt_position = alphabet.index(letter) - shift_amount

#         if decrypt_position < 0:
#             decrypt_position = len(alphabet) + decrypt_position
#             decrypt_message += alphabet[decrypt_position]
#         else:
#             decrypt_message += alphabet[decrypt_position]

#     print(f"decrypt message is: {decrypt_message}")

def caesar(original_message, shift_amount, encode_or_decode):
    caesar_message = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_message:

        if letter not in alphabet:
            caesar_message += letter
        else:
            caesar_position = alphabet.index(letter) + shift_amount
            caesar_position %= len(alphabet)
            caesar_message += alphabet[caesar_position]

    print(f"caesar {encode_or_decode}d message is: {caesar_message}")
     

def main():
    # encrypt(message, shift)
    # decrypt(message, shift)
    should_continue = True
    while should_continue:
        method = input("type 'encode' to encrypt, type 'decode' to decrypt.\n")
        message = input("Type your message.\n")
        shift = int(input("Type the shift number.\n"))
        caesar(message, shift, method)
        restart = input("type 'Yes' if you want to go again, type 'No' if you want to stop.\n").lower()
        if restart == "no":
            should_continue = False
            print("==========Goodbye==========")

if __name__ == '__main__':
    main()

