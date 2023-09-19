alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];


should_continue = True;
def cryptograph(direction, text_input, shift):
    text = "";
    
    if direction == "decode":
        shift *= -1;
        
    for char in text_input:
        
        if char in alphabet:
            position = alphabet.index(char);
            new_position = position + shift;
            text += alphabet[new_position];
        else:
            text += char;
 
    print(f"The {direction}d text is {text}")
    
while should_continue:
    #Cryptogragphy
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n");
    text = input("Type your message:\n").lower();
    shift = int(input("Type the shift number:\n"));

    shift = shift % 26;
    cryptograph(direction = direction, text_input = text, shift = shift); 
    
    result = input("Type 'yes if you want to continue but no if not'").lower();
    
    if result == 'no':
        should_continue = False;
        print("Goodbye");