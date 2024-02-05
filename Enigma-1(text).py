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
        ":":    244
}
definitions = {
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

def encrypt():
    # функция с ключём не реализована
    final = " "
    text = input("Enter text to encrypt: ")
    key = random.randint(0, 256)
    for i in range(len(text)):
        current_symbol = text[i]
        try:
            final += str(symbols[current_symbol] * key + key*4) + " "
        except KeyError:
            print("ошибка в введённых данных")
    print(final+"\n Encrypted")
    print("Key is:" + str(key))
    l = input("press enter")


def decrypt(current_symbol="", decrypted_text=""):
    text = input("Enter text to decrypt: ") + " "
    key = int(input("input key: "))
    for i in range(len(text)):
        if text[i] != " ":
            current_symbol += str(text[i])
        else:
            try:
                current_symbol_decrypted = (int(current_symbol) - key*4) / key
                decrypted_text += str(definitions[int(current_symbol_decrypted)])
                current_symbol = ""
            except TypeError:
                print("ошибка в введёных данных")
            except ValueError:
                print("произошла ошибка")
            except KeyError:
                print("ошибка в введённых данных")

    print(decrypted_text+"\n Decrypted")
    l = input("press enter")


choose = int(input("1.Encrypt \n2.Decrypt\n"))

if choose == 1:
    encrypt()
elif choose == 2:
    decrypt()
else:
    print("write 1 or 2")
