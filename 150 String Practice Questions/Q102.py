'''
102Reverse a string using recursion. 
S = "abc" 
"cba"

'''

s = input("Enter string = ")

rev = ""
i = len(s) - 1

while i >= 0:
    rev += s[i]
    i -= 1

print(rev)