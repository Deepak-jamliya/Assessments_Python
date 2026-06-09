'''
114Check if one string is a subsequence of another. 
S1 = "ace", S2 = "abcde" 
TRUE

'''

s1 = input("Enter S1 = ")
s2 = input("Enter S2 = ")

i = 0

for ch in s2:
    if i < len(s1) and s1[i] == ch:
        i += 1

if i == len(s1):
    print("TRUE")
else:
    print("FALSE")