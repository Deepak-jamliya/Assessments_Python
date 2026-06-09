'''
72Print all substrings of length n. 
S = "abc", n = 2 
"ab, bc"
'''

s = input("Enter String = ")
n = input("Enter Length = ")

substrings = []

for i in range(len(s) - n + 1):
    substrings.append(s[i:i+n])

print(substrings)