dictionnary_braille = {
    "a" : "O.....",
    "b" : "O.O...",
    "c" : "OO....",
    "d" : "OO.O..",
    "e" : "O..O..",
    "f" : "OOO...",
    "g" : "OOOO..",
    "h" : "O.OO..",
    "i" : ".OO...",
    "j" : ".OOO..",
    "k" : "O...O.",
    "l" : "O.O.O.",
    "m" : "OO..O.",
    "n" : "OO.OO.",
    "o" : "O..OO.",
    "p" : "OOO.O.",
    "q" : "OOOOO.",
    "r" : "O.OOO.",
    "s" : ".OO.O.",
    "t" : ".OOOO.",
    "u" : "O...OO",
    "v" : "O.O.OO",
    "w" : ".OOO.O",
    "x" : "OO..OO",
    "y" : "OO.OOO",
    "z" : "O..OOO",
    " " : "......",
}

def convert_braille(sentence):
    new_text_converted = ""
    compteur = 0
    length_of_sentence = len(sentence)
    for char in sentence:
        if char == 'O' or char == '.':
            compteur = compteur + 1
        if compteur > 6:
            break
    if compteur < 5:
        for char in sentence:
            word = dictionnary_braille[char] 
            new_text_converted += word
    else:
        for 
            word = list(dictionnary_braille.keys())[list(dictionnary_braille.values()).index(sentence)]
            new_text_converted += word

    print(new_text_converted)



convert_braille("OOO...")

#print(list(dictionnary_braille.keys())
    #[list(dictionnary_braille.values()).index("O.OO..")])

