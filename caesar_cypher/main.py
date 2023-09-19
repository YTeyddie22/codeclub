alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n");
text = input("Type your message:\n").lower();
shift = int(input("Type the shift number:\n"));

#Cryptogragphy

def cryptograph(direction, text_input,shift):
    text = "";
    for letter in text_input:
        position = alphabet.index(letter);
        if direction == "encode":
            new_position = position + shift;
        elif direction == "decode":
            new_position = position - shift;
        new_letter = alphabet[new_position];
        text += new_letter;
    print(f"The decoded text is {text}")
cryptograph(direction = direction, text_input = text, shift = shift);