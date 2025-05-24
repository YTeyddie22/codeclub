import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for(index,row) in data.iterrows()}

def generatePhone():
    word = input("Enter the word: ").upper()

    try:
        output = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Add only letters")
        generatePhone()
    else: 
        print(output)

generatePhone()


