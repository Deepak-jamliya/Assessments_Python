'''
140 Implement KMP algorithm for substring search. Text = "abcxabc", Pattern = "abc" 0, 4 (indices)

'''

text = "abcxabc"
pattern = "abc"
m = len(pattern)
n = len(text)
lps = [0] * m
length = 0
i = 1
while i < m:
    if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1
    else:
        if length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
i = j = 0
indices = []
while i < n:
    if text[i] == pattern[j]:
        i += 1
        j += 1
    if j == m:
        indices.append(i - j)
        j = lps[j - 1]
    elif i < n and text[i] != pattern[j]:
        if j != 0:
            j = lps[j - 1]
        else:
            i += 1
print("KMP found at indices:", indices)