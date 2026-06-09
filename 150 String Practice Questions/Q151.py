'''
151 Find the lexicographically previous permutation of a string.
"acb"
"abc"
'''

s = list("acb")
n = len(s)
i = n - 2
while i >= 0 and s[i] <= s[i + 1]:
    i -= 1
if i >= 0:
    j = n - 1
    while s[j] >= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
left, right = i + 1, n - 1
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
print("Previous permutation:", "".join(s))