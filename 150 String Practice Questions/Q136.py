'''
136Check if two strings are one edit distance apart. S1 = "pale", S2 = "ple" TRUE
'''

s1 = "pale"
s2 = "ple"
m = len(s1)
n = len(s2)
result = False
if abs(m - n) > 1:
    result = False
elif m == n:
    diff = 0
    for i in range(m):
        if s1[i] != s2[i]:
            diff += 1
    result = (diff == 1)
else:
    if m < n:
        s1, s2 = s2, s1
        m, n = n, m
    i = j = 0
    diff = 0
    while i < m and j < n:
        if s1[i] != s2[j]:
            diff += 1
            i += 1
        else:
            i += 1
            j += 1
    result = (diff <= 1)
print("One edit distance apart:", result)