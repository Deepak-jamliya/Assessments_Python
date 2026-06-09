'''
94Find the smallest window containing all characters of another string. 
S1 = "ADOBECODEBANC", S2 = "ABC" 
"BANC"
'''

s1 = input("Enter S1 = ")
s2 = input("Enter S2 = ")


smallest = s1

for i in range(len(s1)):
    temp = ""
    for j in range(i, len(s1)):
        temp += s1[j]
        if 'A' in temp and 'B' in temp and 'C' in temp:
            if len(temp) < len(smallest):
                smallest = temp
            break

print(smallest)