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
    for char in sentence:
        if dictionnary_braille[char] != 'o' and dictionnary_braille[char] != '.':
            compteur = compteur + 1
        if compteur > 0:
            word = dictionnary_braille[char] 
            new_text_converted += word
        else:
            word = list(dictionnary_braille.keys())[list(dictionnary_braille.values()).index(sentence)]
            new_text_converted += word

    print(new_text_converted)



convert_braille("O.OO..O.....")
##print(list(dictionnary_braille.keys())
      #[list(dictionnary_braille.values()).index("O.....")])

