#Перестановочный шифр
import random
 
def crypto(s,key):
    random.seed(key)
    ln = len(s)
    keys = random.sample(range(ln),ln)
    out = ''
    for i in keys: out += s[i]
    return out
 
def encrypt(s,key):
    random.seed(key)
    ln = len(s)
    keys = random.sample(range(ln),ln)
    out = [' ' for _ in range(ln)]
    for i,j in zip(keys,s):
        out[i] = j
    return ''.join(out)
 
s1 = crypto('Пример шыфруемой строки\nметодом перестановки',5)
print('crypt:\n'+s1)
print ('encrypt:\n'+encrypt(s1,5))