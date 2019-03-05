import random

arr1=[
	'A','B','C','D','E','F','G','H','I',
	'J','K','L','M','N','O','P','Q','R',
	'S','T','U','V','W','X','Y','Z',\
	'a','b','c','d','e','f','g','h','i',
	'j','k','l','m','n','o','p','q','r',
	's','t','u','v','w','x','y','z'
]

arr2=[]
for i in range(len(arr1)):
	arr2.append(arr1[i])

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
    return out

def change_arr2():
	for i in range(number):
		arr2.append(arr2[0])
		arr2.remove(arr2[0])

print("1) Crypt the text")
print("2) Decrypt text from the fail\n")

try:

	ans=int(input("[*] Write the number:\n[number] > "))

	if ans==1:
		number=int(input("[*] Write the key-number [0-%s]: "%(str(len(arr1)))))

		change_arr2()

		msg=input("\n[*] Write the text:\n[text] >> ")

		msgc=""
		for i in msg:
			for j in range(len(arr1)):
				if i==arr1[j]:
					msgc+=arr2[j]

		s0 =crypto(msgc,5)

		print("\nCrypt-text part_1: "+msgc+"\n")
		print("\nCrypt-text part_2: "+s0+"\n")
		
	elif ans==2:
		number=int(input("[*] Write the key-number [0-%s]: "%(str(len(arr1)))))

		change_arr2()

		msg=input("\n[*] Write the text:\n[text] >> ")

		s0 = encrypt(msg,5)

		msgd=""
		for i in s0:
			for j in range(len(arr1)):
				if i==arr2[j]:
					msgd+=arr1[j]
		print("\n[*] Decrypted text:")
		print("[text] << "+str(msgd))

except ValueError:
	print("Error! Print only Integer numbers!")