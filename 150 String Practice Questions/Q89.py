'''
89Remove 'b' and 'ac' from a string. 
S = "abacbb" 
"c"
'''

s = input("Enter string = ")

result = ""
i = 0

while i < len(s):
    if s[i] == 'b':
        i += 1
    elif s[i] == 'a' and i + 1 < len(s) and s[i + 1] == 'c':
        i += 2
    else:
        result += s[i]
        i += 1

print(result)