'''
142 Implement Z algorithm for substring search. 
Text = "aabaaab", Pattern = "aab" 0, 4 (indices)

'''

text = "aabaaab"
pattern = "aab"
concat = pattern + "$" + text
l = len(concat)
z = [0] * l
left = right = 0
for i in range(1, l):
    if i < right:
        z[i] = min(right - i, z[i - left])
    while i + z[i] < l and concat[z[i]] == concat[i + z[i]]:
        z[i] += 1
    if i + z[i] > right:
        left, right = i, i + z[i]
indices = []
for i in range(len(pattern) + 1, l):
    if z[i] == len(pattern):
        indices.append(i - len(pattern) - 1)
print("Z-algo found at indices:", indices)