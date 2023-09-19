alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n");
text = input("Type your message:\n").lower();
shift = int(input("Type the shift number:\n"));

#Encoder
def encrypt(plain_text, shift_amount):
    cypher_text = "";
    for letter in plain_text:
        position = alphabet.index(letter);
        new_position = position + shift_amount;
        new_letter = alphabet[new_position];
        cypher_text += new_letter;
    print(f"The encoded text is {cypher_text}")

#Decoder
def decrypt(decode_text, shift_amount):
    text_decode = "";
    for letter in decode_text:
        position = alphabet.index(letter);
        new_position = position - shift_amount;
        new_letter = alphabet[new_position];
        text_decode += new_letter;
    print(f"The decoded text is {text_decode}")

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift);
elif direction == "decode":
    decrypt(decode_text=text, shift_amount=shift);
