'''
Check if all characters in a string are unique. 
S1 = "abc", S2 = "abca" 
S1: True, S2: False
'''

s1 = input("Enter s1 = ")
s2 = input("Enter s2 = ")

s1unique = 1
for i in s1:
    count = 0
    for ch in s1:
        if ch == i:
            count+=1
    if count > 1:
        s1unique = 0
        break

unique = 1
for i in s2:
    count = 0
    for ch in s2:
        if ch == i:
            count+=1
    if count > 1:
        unique = 0
        break

if s1unique:
    print("S1 : True")
else:
    print("S1 : False")
if unique:
    print("S2 : True")
else:
    print("S2 : False")