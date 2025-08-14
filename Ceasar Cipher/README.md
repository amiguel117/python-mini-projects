# Caesar Cipher 

A Python implementation of the classic Caesar Cipher encryption and decryption algorithm.

## How It Works
- User chooses whether to **encode** (encrypt) or **decode** (decrypt) a message.
- The program takes a message and a numeric shift value.
- Each letter is shifted forward (encode) or backward (decode) in the alphabet based on the shift.
- Wrap-around is handled using modulo arithmetic.

## Features
- Supports both encoding and decoding.
- Wrap-around logic ensures shifting works at the end of the alphabet.
- Beginner-friendly demonstration of encryption concepts.

Type 'encode' to encrypt, type 'decode' to decrypt:

encode
Type your message:
hello
Type the shift number:
5
Here is the decoded result: mjqqt


## Notes
- Only supports lowercase alphabetic characters.
- Spaces, numbers, and symbols are not handled in this version.
