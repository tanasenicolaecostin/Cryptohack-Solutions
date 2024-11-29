from Crypto.Util.number import *
from pwn  import xor 

hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
nohex = bytes.fromhex(hex)

# print(nohex)

partialsecret = b"crypto{"

# print(bytes_to_long(partialsecret))


partialresult = xor(nohex,partialsecret)

# print(partialresult)


usefulresult = b"myXORkey"


secondresult = xor(nohex, usefulresult)

print(secondresult)