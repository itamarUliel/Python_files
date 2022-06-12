import sys
LETTERS = {
    '....': 'h', '.-': 'a',
    '-...': 'b', '-.-.': 'c',
    '-..': 'd', '.': 'e',
    '..-.': 'f', '--.': 'g',
    '..': 'i', '.---': 'j',
    '-.-': 'k', '.-..': 'l',
    '--': 'm', '-.': 'n',
    '---': 'o', '.--.': 'p',
    '--.-': 'q', '.-.': 'r',
    '...': 's', '-': 't',
    '..-': 'u', '...-': 'v',
    '.--': 'w', '-..-': 'x',
    '-.--': 'y', '--..': 'z',
    '.-.-.-': '.', '..--..':
        '?', '--..--': ',',
    '/': ' '
}


def morse_to_eng():
    global LETTERS
    letters_counter = {}
    try:
        file = sys.argv[1]
        with open(file, 'r') as file:
            result = ""
            for line in file:
                for word in line.split(" "):
                    word = word.replace("\n", "")
                    result += LETTERS[word]
                    try:
                        letters_counter[LETTERS[word]] += 1
                    except KeyError:
                        letters_counter[LETTERS[word]] = 1
    except:
        print("Error in Morse Code")
        exit()
    print(result)
    letters_counter.pop(" ")
    letters_counter = sorted(letters_counter.items(),key=lambda x:x[1], reverse=True)
    result = dict()
    for letter,num in letters_counter:
        try:
            result[num] += letter
        except KeyError:
            result[num] = letter
    for num, letter in result.items():
        print("%s - %s" % ("".join(sorted(letter)), num))


morse_to_eng()
