import random

key = "n0k3y"
# ascii code dari encrypted string cipher yang stringnya seperti ini:"{8@=} H^o1W[_1D[lZDZ^
arr = [34, 123, 56, 1, 64, 61, 125, 32, 72, 30, 94, 111, 12, 0, 13, 49, 87, 91, 95, 29, 49, 68, 91, 108, 19, 90, 68, 90, 94, 4]
# count = 100
flag = ""
# word list
word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}_?@1234567890"

#####   FIX


# fs = open("flag.txt","w")

index=0

for i in range(10000):
    for wl in word:
        if index == 30:
            break
        if ord(wl) ^ ord(key[index % 5]) == arr[index]:
            # fs.write(p)
            flag += wl
            index += 1
            # print(index)
        
print(flag)  
# fs.close()


#####   FIX


######   coding encrypt x0r3d.py

"""

/usr/bin/python3


from base64 import  b64encode


## cipher text yang diberikan

cipher = "Ins4AUA9fSBIHl5vDAANMVdbXx0xRFtsE1pEWl4E"

## cipher text yang diberikan


## function encrypt

def encrypt(plain):
    key = "n0k3y"
    cipher = ""
    for c, i in enumerate(plain):
        cipher += chr(ord(i) ^ ord(key[c % 5]))
    
    print(b64encode(cipher.encode()))

## function encrypt

"""

######   coding encrypt x0r3d.py


######  dump cipher text ke ascii code


"""
from base64 import b64decode

cipherText = "Ins4AUA9fSBIHl5vDAANMVdbXx0xRFtsE1pEWl4E"

chiperText_yang_sudah_di_decode_b64 = b64decode(cipherText)

chiperText_yang_sudah_di_decode_UTF = chiperText_yang_sudah_di_decode_b64.decode()

array = []

for i in chiperText_yang_sudah_di_decode_UTF:
    array.append(ord(i))

print(array)

dan outputnya akan seperti ini:

[34, 123, 56, 1, 64, 61, 125, 32, 72, 30, 94, 111, 12, 0, 13, 49, 87, 91, 95, 29, 49, 68, 91, 108, 19, 90, 68, 90, 94, 4]



"""

######  akhir dari dump cipher text ke ascii code


####    percobaan pertama

"""

for i in range(count):
    print(chr(ord(key[i % 5])))

for c in arr:
    for g in range(count):
            k = random.choice(word)
            # print(ord(k) ^ ord(key[g % 5]))
            # print(k)
            if ord(k) ^ ord(key[g % 5]) == c:
                flag += k[:2]
print(flag)
print(len(word))
for i in range(count):
    print(chr(ord(key[i % 5])))
print(len(word))
for i in range(255):
    if ord("2") ^ i == 1:
        print("ascii text nya",i)
        print("keynya ",chr(i))
index = 0
for i in range():
    print(i)
    for o in :
        if ord(o) ^ ord(key[index % 5]) == arr[index]:
            print("i nya sekarang",i)
            flag += o
            index += 1
print(flag)

"""

#####   percobaan pertama

#####   percobaan kedua

"""

for o in word:
    # print(ord(key[i]))
    # print(y)
    p = random.choice(word)
    # print(ord(p) ^ ord(key[i]) == y)
    if ord(o) ^ ord(key[i]) == y:
        print("y nya",y)
        print(o)
print(flag)
print(len(arr))

"""

#####   percobaan kedua


