'''
71Print all substrings. 
S = "abc" 
"a, b, c, ab, bc, abc"

'''

s = input("Enter string = ")

substrings = ""

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substrings += s[i:j] + " "

print(substrings)