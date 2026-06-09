'''
83Create a string from a byte array. 
Byte[] = {72, 101, 108} 
(ASCII for H, e, l) "Hel"
'''

byte = list(input("Enter Bytes = ").split())

result = ""

for b in byte:
    result = result + chr(b)

print(result)