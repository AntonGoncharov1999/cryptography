import sys
from des import setKey, encryptBlock, decryptBlock, encrypt, decrypt
 
def sanityCheck1():
    x0 =  [0x94, 0x74, 0xb8, 0xe8, 0xc7, 0x3b, 0xca, 0x7d]
    x16 = [0x1b, 0x1a, 0x2d, 0xdb, 0x4c, 0x64, 0x24, 0x38]
    x = x0
    for i in range(16):
        setKey(x)
        if i % 2 == 0:
            x = encryptBlock(x) #  x[i+1] = E(x[i], x[i)
        else:
            x = decryptBlock(x) #  x[i+1] = D(x[i], x[i)
    try:
        assert x == x16
    except AssertionError:
        return False
    return True
 
def sanityCheck2():
    try:
        key = [0x0f, 0x15, 0x71, 0xc9, 0x47, 0xd9, 0xe8, 0x59]
        plaintext = "moia zizn prenadlezit arde"
        ciphertext = encrypt(key, plaintext)
        assert decrypt(key, ciphertext) == plaintext
        print(plaintext)
        print(ciphertext)
    except AssertionError:
        return False
    return True
 
def main():
    if sanityCheck1() and sanityCheck2():
        print("создан для того чтоб проверить работает ли (не забыть удалить)")
    else:
        sys.exit(1)
    sys.exit()
 
if __name__ == '__main__':
    main()