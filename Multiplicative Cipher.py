import numpy as np 
keys_array = [1,3,5,7,9,11,15,17,19,21,23,25]

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1


def encryption(plain_text,keys = None):
	key = keys_array[np.random.randint(len(keys_array))]
	if keys:
		key = keys
	cipher=''
	for ch in plain_text:
		ind = ord(ch)
		ind = ((ind - ord('a'))*key)%26
		cipher += chr(ord('a')+ind)
	return cipher,key

def decryption(cipher_text,keys):
	key = keys
	key = modInverse(key,26)
	plain_text=''
	for ch in cipher_text:
		ind = ord(ch)
		ind = ((ind - ord('a'))*key)%26
		plain_text += chr(ord('a')+ind)
	return plain_text	


plain_text = str(input("Enter the String: "))
cipher,key = encryption(plain_text)
print("Original Text:",plain_text)
print("Cipher Text: {}, Key: {}".format(cipher,key))
print("Decrypted Text",decryption(cipher,key))