import numpy as np 

def encryption(plain_text,keys = None):
	key = np.random.randint(26)
	if keys:
		key = keys
	cipher=''
	for ch in plain_text:
		ind = ord(ch)
		ind = (ind - ord('a') + key)%26
		cipher += chr(ord('a')+ind)
	return cipher,key

def decryption(cipher_text,keys):
	key = keys
	plain_text=''
	for ch in cipher_text:
		ind = ord(ch)
		ind = (ind - ord('a') - key)%26
		plain_text += chr(ord('a')+ind)
	return plain_text	


plain_text = str(input("Enter the String: "))
cipher,key = encryption(plain_text)
print("Original Text",plain_text)
print("Cipher Text: {}, Key: {}".format(cipher,key))
print("Decrypted Text",decryption(cipher,key))