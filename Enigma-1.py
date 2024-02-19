import random
symbols = {
        "1":    7,
        "2":    269,
        "3":    10,
        "4":    52,
        "5":    95,
        "6":    77,
        "7":    80,
        "8":    45,
        "9":    88,
        "0":    72,
        "a":    9,
        "b":    93,
        "c":    44,
        "d":    245,
        "e":    254,
        "f":    166,
        "g":    150,
        "h":    18,
        "i":    121,
        "j":    32,
        "k":    86,
        "l":    120,
        "m":    12,
        "n":    136,
        "o":    144,
        "p":    188,
        "q":    46,
        "r":    219,  
        "s":    289,
        "t":    315,
        "u":    125,
        "v":    75,
        "w":    85,
        "x":    161,
        "y":    110,
        "z":    96,
        "A":    9,
        "B":    93,
        "C":    44,
        "D":    245,
        "E":    254,
        "F":    166,
        "G":    150,
        "H":    18,
        "I":    121,
        "J":    32,
        "K":    86,
        "L":    120,
        "M":    12,
        "N":    136,
        "O":    144,
        "P":    188,
        "Q":    46,
        "R":    219,
        "S":    289,
        "T":    315,
        "U":    125,
        "V":    75,
        "W":    85,
        "X":    161,
        "Y":    110,
        "Z":    96,
        "А":    4,    
        "Б":    8,
        "В":    2,
        "Г":    42,
        "Д":    17,
        "Е":    1,
        "Ё":    41,
        "Ж":    30,
        "З":    23,
        "И":    57,
        "Й":    410,
        "К":    3,
        "Л":    13,
        "М":    24,
        "Н":    403,
        "О":    217,
        "П":    213,
        "Р":    53,
        "С":    5,
        "Т":    112,
        "У":    6,
        "Ф":    61,
        "Х":    25,
        "Ц":    212,
        "Ч":    313,
        "Ш":    412,
        "Щ":    33,
        "Ь":    712,
        "Ы":    700,
        "Ъ":    612,
        "Э":    470,
        "Ю":    450,
        "Я":    730,
        "а":    4,
        "б":    8,
        "в":    2,
        "г":    42,
        "д":    17,
        "е":    1,
        "ё":    41,
        "ж":    30,
        "з":    23,
        "и":    57,
        "й":    410,
        "к":    3,
        "л":    13,
        "м":    24,
        "н":    403,
        "о":    217,
        "п":    213,
        "р":    53,
        "с":    5,
        "т":    112,
        "у":    6,
        "ф":    61,
        "х":    25,
        "ц":    212,
        "ч":    313,
        "ш":    412,
        "щ":    33,
        "ь":    712,
        "ы":    700,
        "ъ":    612,
        "э":    470,
        "ю":    450,
        "я":    730,
        ".":    91,
        ",":    114,
        "!":    38,
        "?":    296,
        " ":    29,
        "-":    97,
        "(":    19,
        ")":    668,
        "@":    115,
        '"':    73,
        ":":    244,
        "'":    74,
        '"':    104
}
definitions = {
        9:      "a", 
        93:     "b",
        44:     "c",
        245:    "d",
        254:    "e",
        166:    "f",
        150:    "g",
        18:     "h",
        121:    "i",
        32:     "j",
        86:     "k",
        120:    "l",
        12:     "m",
        136:    "n",
        144:    "o",
        188:    "p",
        46:     "q",
        219:    "r",
        289:    "s",
        315:    "t",
        125:    "u",
        75:     "v",
        85:     "w",
        161:    "x",
        110:    "y",
        96:     "z",
        4:      "а",
        8:      "б",
        2:      "в",
        42:     "г",
        17:     "д",
        1:      "е",
        41:     "ё",
        30:     "ж",
        23:     "з",
        57:     "и",
        410:    "й",
        3:      "к",
        13:     "л",
        24:     "м",
        403:    "н",
        217:    "о",
        213:    "п",
        53:     "р",
        5:      "с",
        112:    "т",
        6:      "у",
        61:     "ф",
        25:     "х",
        212:    "ц",
        313:    "ч",
        412:    "ш",
        33:     "щ",
        712:    "ь",
        700:    "ы",
        612:    "ъ",
        470:    "э",
        450:    "ю",
        730:    "я",
        91:     ".",
        114:    ",",
        38:     "!",
        296:    "?",
        29:     " ",
        97:     "-",
        19:     "(",
        668:    ")",
        115:    "@",
        73:     '"',
        244:    ":",
        74:     "'",
        104:    '"',
        7:      "1",
        269:    "2",
        10:     "3",
        52:     "4",
        95:     "5",
        77:     "6",
        80:     "7",
        45:     "8",
        88:     "9",
        72:     "0"
}

def chargen(key):
    Fkey = ""
    if key == 1:
        Fkey = "w"
    elif key == 2:
        Fkey = "x"
    elif key == 3:
        Fkey = "m"
    elif key == 4:
        Fkey = "k"
    elif key == 5:
        Fkey = "l"
    elif key == 6:
        Fkey = "a"
    elif key == 7:
        Fkey = "z"
    elif key == 8:
        Fkey = "c"
    elif key == 9:
        Fkey = "u"
    elif key == 10:
        Fkey = "t"
    return Fkey

def chardegen(key):
    Fkey = ""
    if key == "w":
        Fkey = 1
    elif key == "x":
        Fkey = 2
    elif key == "m":
        Fkey = 3
    elif key == "k":
        Fkey = 4
    elif key == "l":
        Fkey = 5
    elif key == "a":
        Fkey = 6
    elif key == "z":
        Fkey = 7
    elif key == "c":
        Fkey = 8
    elif key == "u":
        Fkey = 9
    elif key == "t":
        Fkey= 10
    return Fkey

def keygen(key1,key2,key3,key1l,key2l,key3l):
    k1 = chargen(key1l)
    k2 = chargen(key2l)
    k3 = chargen(key3l)
    enc_key1 = (key1*key1l)-key2l
    enc_key2 = (key2+key2l)-key3l
    enc_key3 = (key3-key3l)*key1l
    FinKey = str(enc_key1) + k1 + str(enc_key2) + k2 + str(enc_key3) + k3 
    return FinKey

def keydegen(key): 
    global numb
    numb = []
    let = []
    dec_let = []
    dec_key1 = ""
    dec_key2 = ""
    dec_key3 = ""
    for i in range(len(key)):
        if key[i] != "w" and key[i] != "m" and key[i] != "k" and key[i] != "x" and key[i] != "l" and   key[i] != "z" and key[i] != "c" and key[i] != "t" and key[i] != "u" and key[i] != "a":
            if len(let) == 0:
                dec_key1+=(key[i])
            elif len(let) == 1:
                dec_key2+=(key[i])
            elif len(let) == 2:
                dec_key3+=(key[i])
        else:
            let.append(key[i])
    for i in range(len(let)):
        dec_let.append(chardegen(let[i]))
    dec_key1 = (int(dec_key1) + int(dec_let[1])) / int(dec_let[0])
    dec_key2 = (int(dec_key2) + int(dec_let[2])) - int(dec_let[1])
    dec_key3 = (int(dec_key3) / int(dec_let[0])) + int(dec_let[2])
    numb.append(int(dec_key1))
    numb.append(int(dec_key2))
    numb.append(int(dec_key3))

def encrypt():
    # функция с ключём не реализована(реализация 15.02.24)
    quest = input("Введите ключ шифрования(если отсутствует - оставьте поле пустым):")
    if quest == "":
        pass
    else:
        final = ""
        FinKey = quest
        keydegen(FinKey)
        text = input("Введите текст: ")
        for i in range(len(text)):
            current_symbol = text[i]
            try:
                final += str(symbols[current_symbol] * numb[0] + numb[1] * 4 - numb[2]) + " "
            except KeyError:
                print("ошибка в введённых данных")
        print(final+"\n Зашифровано")
        l = input("Нажмите Enter")

    final = " "
    text = input("Введите текст: ")
    key1 = random.randint(1, 256)
    key2 = random.randint(1, 256)
    key3 = random.randint(1, 256)
    key_let1 = random.randint(1,10)
    key_let2 = random.randint(1,10)
    key_let3 = random.randint(1,10)
    FinKey = keygen(key1,key2,key3,key_let1,key_let2,key_let3)
    for i in range(len(text)):
        current_symbol = text[i]
        try:
            final += str(symbols[current_symbol] * key1 + key2*4 -key3) + " "
        except KeyError:
            print("ошибка в введённых данных")
    print(final+"\n Зашифровано")
    print("Ключ: ",FinKey)
    l = input("Нажмите Enter")

def decrypt(current_symbol="", decrypted_text=""):
    text = input("Введите текст: ") + " "
    key = input("Введите ключ: ")
    keydegen(key)
    for i in range(len(text)):
        if text[i] != " ":
            current_symbol += str(text[i])
        else:
            try:
                current_symbol_decrypted = (int(current_symbol) + numb[2] - numb[1]*4) / numb[0]
                decrypted_text += str(definitions[int(current_symbol_decrypted)])
                current_symbol = ""
            except TypeError:
                print("ошибка в введёных данных")
            except ValueError:
                pass
            except KeyError:
                print("ошибка в введённых данных")

    print(decrypted_text+"\n Дешифровано")
    l = input("Нажмите Enter")

choose = int(input("1.Шифрование \n2.Дешифрование\n"))

if choose == 1:
    encrypt()
elif choose == 2:
    decrypt()
else:
    print("Введите 1 или 2")