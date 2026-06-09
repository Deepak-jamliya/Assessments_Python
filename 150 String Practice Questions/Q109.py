'''
109Find the lexicographically smallest substring of length k. 
S = "banana", k = 3 
"ana"
'''

s = input("Enter String = ")
k = 3

smallest = s[0:k]

for i in range(1, len(s) - k + 1):
    sub = s[i:i+k]
    if sub < smallest:
        smallest = sub

print(smallest)