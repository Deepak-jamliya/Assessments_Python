'''
137Find the length of the longest substring with at most k distinct characters. S = "eceba", k = 2 3 ("ece")

'''

s = "eceba"
k = 2
max_len = 0
max_sub = ""
for i in range(len(s)):
    distinct = {}
    for j in range(i, len(s)):
        distinct[s[j]] = distinct.get(s[j], 0) + 1
        if len(distinct) <= k:
            if j - i + 1 > max_len:
                max_len = j - i + 1
                max_sub = s[i:j+1]
        else:
            break
print("Longest substring with at most", k, "distinct chars:", max_sub)