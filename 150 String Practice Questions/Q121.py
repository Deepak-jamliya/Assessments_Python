'''
121Check if a string contains only binary digits (0/1). 
S1 = "1010", S2 = "102" 
S1: True, S2: False
'''

s1 = input("Enter String = ")
s2 = input("Enter String = ")

find = True
for i in s1:
    if i!= '0' and i!= '1':
        find = False
        break

print("S1 : ",find)

find = True
for i in s2:
    if i!= '0' and i!= '1':
        find = False
        break

print("S2 : ",find)