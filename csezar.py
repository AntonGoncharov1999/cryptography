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

def change_arr2():
	for i in range(number):
		arr2.append(arr2[0])
		arr2.remove(arr2[0])

print("1) Crypt the text/file")
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
		crypt=open("text_crypt.txt","w")
		print("\nCrypt-text: "+msgc+"\n")
		crypt.write(msgc)
		crypt.close()

		print(arr1)
		print()
		print(arr2)

	elif ans==2:
		number=int(input("[*] Write the key-number [0-%s]: "%(str(len(arr1)))))

		change_arr2()

		decrypt_r=open("text_crypt.txt","r")
		read=decrypt_r.read()
		msgd=""
		for i in read:
			for j in range(len(arr1)):
				if i==arr2[j]:
					msgd+=arr1[j]
		print("\n[*] Decrypted text:")
		print("[text] << "+str(msgd))
		answer=input("\n[*] Save decrypted text in the file?\n[y/n] > ")
		if answer=="y" or answer=="Y":
			decrypt_w=open("text_decrypt.txt","w")
			decrypt_w.write(msgd)
			decrypt_w.close()
			print("\n[+] File 'text_decrypt.txt' successfully saved! ")
		else:
			pass
		decrypt_r.close()

except ValueError:
	print("Error! Print only Integer numbers!")