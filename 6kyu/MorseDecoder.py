# kata: https://www.codewars.com/kata/54b724efac3d5402db00065e

# decode_morse('.... . -.--   .--- ..- -.. .')
# Should return "HEY JUDE"

# from preloaded import MORSE_CODE
# Had to make my own dictionary
# Use the preloaded module for codewars

MORSE_CODE = {
    '.-':'A',
    '-...':'B',
    '-.-.':'C',
    '-..':'D',
    '.':'E',
    '..-.':'F',
    '--.':'G',
    '....':'H',
    '..':'I',
    '.---':'J',
    '-.-':'K',
    '.-..':'L',
    '--':'M',
    '-.':'N',
    '---':'O',
    '.--.':'P',
    '--.-':'Q',
    '.-.':'R',
    '...':'S',
    '-':'T',
    '..-':'U',
    '...-':'V',
    '.--':'W',
    '-..-':'X',
    '-.--':'Y',
    '--..':'Z',
    '':' ',
    '...---...':'SOS!'
}

def decode_morse(morse_code):
    res = ""
    word_arr = morse_code.split("   ")
    for word in word_arr:
        if word == "":
            continue
        chr_arr = word.split()
        for chr in chr_arr:
            res = res + MORSE_CODE[chr]
        res = res + " "
    return res.strip()