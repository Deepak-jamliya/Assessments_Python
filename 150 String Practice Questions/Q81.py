'''
81Generate a hash code or UUID. 
S = "test" 
Hash: 3556498 (Example hash code)
'''

s = input("Enter  String = ")
hash_value = 0

for ch in s:
    hash_value = hash_value * 31 + ord(ch)

print("Hash:", hash_value)