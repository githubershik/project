import random
x = open("test.txt", "r+")
z = x.read()
l = ""
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