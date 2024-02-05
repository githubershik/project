import random
symbols = {
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
        "-":    97
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
        97:     "-"
}


def encrypt():
    # функция с ключём не реализована
    choosenc=int(input("работа с текстом или файлом?\n1.текст\n2.файл"))
    if choosenc == 1:
        filename = input("введите название файла")
        
    else:
        final = " "
        hopa = input("Enter text to encrypt: ")
        key = random.randint(0, 256)
        for i in range(len(hopa)):
            bock = hopa[i]
            try:
                final += str(symbols[bock] * key + key*4) + " "
            except KeyError:
                print("ошибка в введённых данных")
        print(final+"\n Encrypted")
        print("Key is:" + str(key))
        l = input("press enter")


def decrypt(boba="", pivo=""):
    biba = input("Enter text to decrypt: ") + " "
    key = int(input("input key: "))
    for i in range(len(biba)):
        if biba[i] != " ":
            boba += str(biba[i])
        else:
            try:
                jopa = (int(boba) - key*4) / key
                pivo += str(definitions[int(jopa)])
                boba = ""
            except TypeError:
                print("ошибка в введёных данных")
            except ValueError:
                print("произошла ошибка")
            except KeyError:
                print("ошибка в введённых данных")

    print(pivo+"\n Decrypted")
    l = input("press enter")


choose = int(input("1.Encrypt \n2.Decrypt\n"))

if choose == 1:
    encrypt()
elif choose == 2:
    decrypt()
else:
    print("write 1 or 2")
