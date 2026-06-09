'''
107Check if a string is a pangram (contains every letter). 
S = "The quick brown fox jumps over the lazy dog" 
TRUE
'''

s = input("Enter string = ")

seen = set()
for c in s:
    if 'a' <= c <= 'z':
        seen.add(c)
    elif 'A' <= c <= 'Z':
        seen.add(chr(ord(c) + 32))

print(len(seen) == 26)
