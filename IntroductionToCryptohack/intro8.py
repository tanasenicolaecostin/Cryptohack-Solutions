from Crypto.Util.number import *
from pwn  import xor 
hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

nohex = bytes.fromhex(hex)

print(nohex)



for n in range(0,256):
    flag = xor(n, nohex)
    
    if "crypto" in str(flag):
        print(flag)