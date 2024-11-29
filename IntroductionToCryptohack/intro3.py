import base64

hexstring = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

nohex = bytes.fromhex('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')

print (nohex)

encoded = base64.b64encode(nohex)

print(encoded)