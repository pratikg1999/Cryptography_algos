import random
# cPBpx = [[random.shuffle([i*8+j for j in range(8)]) for  i in range(6)] #for 56 to 48 bits
cPBox = [14,17,11,24,1,5, 3,28,15,6,21,10, 23,19,12,4,26,8, 16,7,27,20,13,2, 41,52,31,37,47,55, 30,40,51,45,33,48, 44,49,39,56,34,53, 46,42,50,36,29,32 ]
parityTable = [ 57,49,41,33,25,17,9, 1,58,50,42,34,26,18, 10,2,59,51,43,35,27, 19,11,3,60,52,44,36,           63,55,47,39,31,23,15, 7,62,54,46,38,30,22, 14,6,61,53,45,37,29, 21,13,5,28,20,12,4 ]
finalPermTable = [40,8,48,16,56,24,64,32, 39,7,47,15,55,23,63,31, 38,6,46,14,54,22,62,30, 37,5,45,13,53,21,61,29, 36,4,44,12,52,20,60,28, 35,3,43,11,51,19,59,27, 34,2,42,10,50,18,58,26, 33,1,41,9,49,17,57,25 ]
initialPermTable = [58,50,42,34,26,18,10,2, 60,52,44,36,28,20,12,4, 62,54,46,38,30,22,14,6, 64,56,48,40,32,24,16,8, 57,49,41,33,25,17,9,1, 59,51,43,35,27,19,11,3, 61,53,45,37,29,21,13,5, 63,55,47,39,31,23,15,7 ]
straightPBox = [16,7,20,21, 
        29,12,28,17, 
        1,15,23,26, 
        5,18,31,10, 
        2,8,24,14, 
        32,27,3,9, 
        19,13,30,6, 
        22,11,4,25 ]
sBoxes = [[
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7, ],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8, ],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0, ],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13 ],
    ], 
    [ 
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10, ],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5, ],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15, ],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9 ],
    ], 
  
  
    [ 
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8, ],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1, ],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7, ],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12 ],
    ], 
    [ 
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15, ],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9, ],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4, ],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14 ],
    ], 
    [ 
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9, ],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6, ],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14, ],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3 ],
    ], 
    [ 
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11, ],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8, ],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6, ],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13 ],
    ], 
    [ 
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,] ,
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,] ,
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,] ,
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12 ],
    ], 
    [ 
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,] ,
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,] ,
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,] ,
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11 ],
    ]]

def lefCircularShift(b, n):
    ans =b[n:len(b)]
    ans+=b[:n]
    return ans
def permute(plain, dBox):
    ans=""
    for i in range(len(dBox)):
        # print(i, dBox[i]-1)
        ans+=plain[dBox[i]-1]
    return ans
def goThroughS(part, n):
    row = int(part[0]+part[5], 2)
    col = int(part[1:5],2)
    binAns = bin(sBoxes[n][row][col])[2:]
    return "0"*(4-len(binAns)) + binAns
def expand(r32):
    r48 = [None]*48
    for i in range(8):
        for j in range(4):
            r48[i*6+j+1] = r32[i*4 + j]
        r48[((i-1)%8)*6 + 5] = r32[i*4] 
        r48[((i+1)%8)*6] = r32[i*4+3]
    # print(r48)
    return ''.join(r48)
def xor(a32, b32):
    ans =""
    for i in range(32):
        ans += str(int(a32[i])^int(b32[i]))
    return ans

def fiestal(r32, key):
    r48 = expand(r32)
    # print(r48)
    # print(int(r48,2))
    # print(key)
    # print(bin(int(r48,2)^0)[2:])
    temp = str(bin(int(r48,2)^int(key, 2))[2:])
    r48 = "0"*(48-len(temp))+temp
    # print(r48)
    afterS = ""
    for i in range(8):
        part = r48[i*6:i*6+6]
        out = goThroughS(part, i)
        # print(part, out)
        afterS+=out
    ans=""
    for i in range(len(straightPBox)):
        ans+=afterS[straightPBox[i]-1]
    return ans
    
def fiestalRound(plain, key):
    l = plain[:32]
    r = plain[32:]
    fres = fiestal(r, key)
    l = xor(l, fres)
    ans = r+l
    return ans

def goThroughCompression(p):
    ans=""
    # print(len(p))
    for i in range(48):
        ans+= p[cPBox[i]-1]
    return ans
def genKeys(key56):
    l = key56[:28]
    r = key56[28:]
    roundKeys=[]
    for i in range(16):
        if(i+1==1 or i+1==2 or i+1==9 or i+1==16):
            l = lefCircularShift(l, 1)
            r = lefCircularShift(r, 1)
        else:
            l = lefCircularShift(l, 2)
            r = lefCircularShift(r, 2)
        # print(len(l), len(r))
        roundKeys.append(goThroughCompression(l+r))
    return roundKeys
def convertToAscii(word):
    bin64 = ""
    for i in word:
        asci = bin(ord(i))[2:]
        bin64+=("0"*(8-len(asci))  + asci)
    return bin64
def convertToWord(bin64):
    # print(bin64)
    word = ""
    for i in range(0, 64, 8):
        # print(i, bin64[i:i+8])
        word+=chr(int(bin64[i:i+8],2))
    return word

def swapper(p):
    return p[32:]+p[:32]


plain = input("Enter the 8 character plain text: ")
plain = convertToAscii(plain)
print("The 64-bit plain text is", plain)
k = input("Enter the 8 character key: ")
k = convertToAscii(k)
print("The 64 bit key is", k)
# k="1010101010111011000010010001100000100111001101101100110011011101"
# k="0000111000110010100100100011001011101010011011010000110101110011"
# print(len(k))
key = ""
for i in range(len(parityTable)):
    key+=k[parityTable[i]-1]
# print(len(key))
roundKeys=genKeys(key)
# print(roundKeys)
# a='0001001000110100010101101010101111001101000100110010010100110110'

# print(fiestalRound(a, "001101100001010001100100011110001110000111100001"))

# a= ""
# for i in range(64):
#     a+=str(random.randint(0,1))
# print(a ,len(a))
p=plain
p = permute(p, initialPermTable)
for i in range(16):
    p = fiestalRound(p, roundKeys[i])
    # print(i, hex(int(p[:32],2))[2:], hex(int(p[32:],2))[2:], len(p), hex(int(roundKeys[i],2))[2:])

enc = swapper(p)
# print(len(enc))
enc = permute(enc, finalPermTable)
print()
print("The ecrypted text is", enc)
dec = enc
dec = permute(enc, initialPermTable)
for i in range(16):
    dec = fiestalRound(dec, roundKeys[15-i])
    # print(dec)


dec = swapper(dec)
dec = permute(dec, finalPermTable)
print("The decryption is ",dec,"which is", convertToWord(dec))
