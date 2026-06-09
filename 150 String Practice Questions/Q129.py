'''
129Find the smallest window containing all distinct characters.
 S = "aabcbde" 
 "aabcbde"

'''
s = "aabcbde"

distinct = ""
for ch in s:
    if ch not in distinct:
        distinct += ch

min_len = len(s)
result = s

for i in range(len(s)):
    seen = ""
    for j in range(i, len(s)):
        if s[j] not in seen:
            seen += s[j]
        if len(seen) == len(distinct):
            if j - i + 1 < min_len:
                min_len = j - i + 1
                result = s[i:j+1]
            break

print(result)