'''
77Find the longest substring that appears at both ends. 
S = "abracadabra" 
"abra"
'''

s = input("Enter String = ")

n = len(s)
result = ""

for i in range(1, n):
    prefix = s[:i]
    suffix = s[n - i:]
    if prefix == suffix:
        result = prefix

print(result)