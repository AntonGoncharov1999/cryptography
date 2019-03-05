def cript():
        txt = "ERROR"
        print("Isshodnie message: " + txt)
        key = "PAN"

        key*= len(txt) // len(key) + 1

        st = ""

        for i, j in enumerate(txt):
                res = ( ord(j) + ord(key[i]) )
                st += chr( res % 26 + ord('A') )
        print( "Encripted message: " + str(st) )
        
def decript():
        txt = "TREDR"
        print("Isshodnie message: " + txt)
        key = "PAN"

        key*= len(txt) // len(key) + 1

        st = ""

        for i, j in enumerate(txt):
                res = ( ord(j) - ord(key[i]) )
                st += chr( res % 26 + ord('A') )
        print( "Encripted message: " + str(st) )   


print('зашифровать сообщение(0) или разшифровать(1)')

a = input()

if a == '0':
        cript()
elif a == '1':
        decript()
else:
        print('notverno')
