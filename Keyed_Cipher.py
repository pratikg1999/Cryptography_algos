import numpy as np

Original_message = str(input('Enter Message: '))
print("Original Message: ",Original_message)

block_length = int(input('Enter Block Length: '))

key = np.arange(0,block_length)
key = np.random.permutation(key)
print("Key: {}".format(key))

def encryption(Original_message,key=None):
	Original_message = ''.join(Original_message.split(' '))
	L = len(Original_message)

	if key is None:
		key = np.array([2,0,3,4,1])

	# print(key)
	block_length = len(key)
	pad_length = block_length -  L%block_length
	cipher = Original_message

	
	for i in range(pad_length):
		cipher+='~'

	print("Padded Message:",cipher)
	cipher_length = len(cipher)
	num_blocks = cipher_length//block_length
	encrypted_block = []
	base_ind = 0
	for i in range(num_blocks):
		base_ind =i*block_length
		temp = []
		for j in range(block_length):
			temp.append(cipher[base_ind+key[j]])
		encrypted_block.append(temp)
	cipher = ''
	for a in encrypted_block:
		cipher+=''.join(a)
		cipher+=' '

	return cipher

def decryption(cipher,key=None):
	cipher = ''.join(cipher.split(' '))
	L = len(cipher)

	if key is None:
		key = np.array([2,0,3,4,1])
	block_length = len(key)

	key1 = np.zeros(key.shape)

	for i in range(block_length):
		key1[key[i]]=i
	key1 = np.array(list(map(int,key1)))
	# print(key1)

	cipher_length = len(cipher)

	num_blocks = cipher_length//block_length
	encrypted_block = []
	base_ind = 0

	for i in range(num_blocks):
		base_ind =i*block_length
		temp = []
		for j in range(block_length):
			temp.append(cipher[base_ind+key1[j]])
		encrypted_block.append(temp)

	cipher = ''
	for a in encrypted_block:
		cipher+=''.join(a)
		cipher+=' '

	return cipher


cipher = encryption(Original_message,key)
print("Cipher Message: ",cipher)
print("Decrypted Message:",decryption(cipher,key))











