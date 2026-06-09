'''
115Find the edit distance (Levenshtein distance) between two strings. 
S1 = "kitten", S2 = "sitting" 
3
'''

s1 = input("Enter S1 = ")
s2 = input("Enter S2 = ")

i = 0
count = 0

while i < len(s1) and i < len(s2):
    if s1[i] != s2[i]:
        count += 1 
    i += 1

count += abs(len(s1) - len(s2))

print(count)