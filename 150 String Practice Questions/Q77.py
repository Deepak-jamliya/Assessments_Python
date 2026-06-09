'''
78Find the longest mirror-image substring at both ends. 
S = "aabccbaa" 
"aab"
'''

s = input("Enter String = ")
n = len(s)

result = ""

for i in range(1, n // 2 + 1):
    prefix = s[:i]
    suffix = s[n - i:]
    if prefix == suffix[::-1]:
        result = prefix

print(result)