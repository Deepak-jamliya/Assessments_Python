'''
118Find the longest repeated substring. 
S = "banana" 
"ana"

'''

s = input("Enter String = ")

longest = ""

n = len(s)
for i in range(n):
    for j in range(i + 1, n + 1):
        sub = s[i:j]
        if s.count(sub) > 1 and len(sub) > len(longest):
            longest = sub

print(longest)