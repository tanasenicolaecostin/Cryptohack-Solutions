import base64
import pwntools

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key21 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key32 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
key321f = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")


key2 = pwntools.xor(key21, key1)

print(key2)