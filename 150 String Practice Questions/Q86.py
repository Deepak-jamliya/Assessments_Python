'''
86Print all permutations of a string without repetition. 
S = "ab" 
"ab", "ba"
'''

s = input("Enter string = ")

a = s[0]
b = s[1]

temp = a
a = b
b = temp

print(s[0] + s[1])
print(a + b)