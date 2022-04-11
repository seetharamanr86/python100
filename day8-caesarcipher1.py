alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26
text_length = len(text)
repeat="yes"

def caesar(encode = direction, text_length = text_length, shift = shift):
    if encode=="encode":
        encode_text = ""
        for i in range(0, text_length):
            try:
                shift_index=alphabet.index(text[i])+shift
                if shift_index>25:
                    shift_index=shift_index-26
                encode_text=encode_text+alphabet[shift_index]
            except ValueError:
                encode_text = encode_text + text[i]
        print(f"Encoded text is: {encode_text}")
    else:
        decode_text = ""
        for i in range(0, text_length):
            try:
                shift_index=alphabet.index(text[i])-shift
                if shift_index<0:
                    shift_index=shift_index+26
                decode_text=decode_text+alphabet[shift_index]
            except ValueError:
                decode_text = decode_text + text[i]
        print(f"Decoded text is: {decode_text}")

while repeat=="yes":
    caesar(encode = direction, text_length = text_length, shift = shift)
    repeat=input("Do you like to repeat? 'yes' or 'no': ").lower()
    if repeat=="yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        text_length = len(text)

