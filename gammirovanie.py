from itertools import zip_longest, cycle
 
 
def xor_crypt_string(data: str, key: str):
    xored = ''
    for (x, y) in zip_longest(data, cycle(key)):
        if not x:
            break
        xored += chr(ord(x) ^ ord(y))
    return xored
 
 
a = xor_crypt_string('орда', '123')
print(a)
print(xor_crypt_string(a, '123'))