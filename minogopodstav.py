import sys

# Исходный алфавит. Создаем из него массив
rualf = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
alf = []
for x in rualf:
    alf.append(x)
print ("Original alf:",rualf)

# Первый подстановочный алфавит
first = "БЮГЫЕЬЗШЙЦЛФНТПРСОУМХКЧИЩЖЪДЭВЯ АЁ"
firstalf=[]
for x in first:
    firstalf.append(x)
print ("First alf:",first)

#Второй подстановочный алфавит
second = "СОУМКХЧИЩЖЪДЭВЯАБЮГ ЕЬЗШЙЦЁФНТПРЫЛ"
secondalf = []
for x in second:
    secondalf.append(x)
print ("Second alf:",second)

# Третий подстановочный алфавит
third = "МНОПРСТУФХЦЧШЩЪЬЫЭЮЯ АБВГДЕЁЖЗИЙКЛ"
thirdalf = []
for x in third:
    thirdalf.append(x)
print ("Third alf:",third)

# Функция кодирования
def crypt(inp):
    out = ""
    i = 1
    try:
        for x in inp:
            if (i%3==0):
                y = rualf.index(x)
                out += thirdalf[y]
            elif (i%2==0):
                y = rualf.index(x)
                out += secondalf[y]
            else:
                y = rualf.index(x)
                out += firstalf[y]
            i += 1
    except:
        print ("Обнаружен символ, которого нет в исходном алфавите (русский).")
        sys.exit()
    return out

# Функция декодирования
def decrypt(cryptotext):
    out2 = ""
    i = 1
    for x in cryptotext:
        if (i%3==0):
            y = third.index(x)
            out2 += alf[y]
        elif (i%2==0):
            y = second.index(x)
            out2 += alf[y]
        else:
            y = first.index(x)
            out2 += alf[y]
        i += 1
    return out2

#Главная функция
def main():
    print ("Please enter Original text:")
    inp = input()
    print ("Original text: ",inp)
    cryptotext = crypt(inp)
    print ("Crypt text: ",cryptotext)
    decryptotext = decrypt(cryptotext)
    print ("Decrypt text: ",decryptotext)

main()