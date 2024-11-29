string = 'label'

integer = 13

stringnum = []

xorarray = []

finstring = ''

for n in string:
    stringnum.append(ord(n))

for n in stringnum:
    xorarray.append(n ^ 13)

for n in xorarray:
    finstring += chr(n)

print(finstring)

