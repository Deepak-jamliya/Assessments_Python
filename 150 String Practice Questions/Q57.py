'''
57Merge two strings alternatively (char by char). 
S1 = "ABC", S2 = "def" 
"AdBeCf"
'''

s1 = input("Enter String = ")
s2 = input("Enter String = ")


result = ""
i = 0

while i < len(s1) or i < len(s2):
    if i < len(s1):
        result += s1[i]
    if i < len(s2):
        result += s2[i]
    i += 1

print(result)