'''
146Compress a string using run-length encoding. S = "aaabbc" "a3b2c1"

'''

s = "aaabbc"
result = ""
i = 0
while i < len(s):
    count = 1
    while i + count < len(s) and s[i + count] == s[i]:
        count += 1
    result += s[i] + str(count)
    i += count
print("Compressed:", result)