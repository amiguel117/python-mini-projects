from operator import index
from pydoc import plaintext

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasar(direction, original_text, shift_amount):
    cipher_text = ''
    if direction == 'encode':
        for letters in original_text:
            shifted_letters = (alphabet.index(letters) + (shift_amount)) % len(alphabet)
            cipher_text += alphabet[shifted_letters]
        print(f'Here is the {direction} result: {cipher_text}')
    elif direction == 'decode':
        for letters in original_text:
            shifted_letters = (alphabet.index(letters) + (shift_amount * -1)) % len(alphabet)
            cipher_text += alphabet[shifted_letters]
        print(f'Here is the {direction} result: {cipher_text}')



ceasar(direction, original_text=text, shift_amount=shift)
