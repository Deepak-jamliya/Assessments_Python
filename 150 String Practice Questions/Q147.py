'''
147Decompress a run-length encoded string. S = "a3b2c1" "aaabbc"
'''

s = "a3b2c1"
result = ""
i = 0
while i < len(s):
    ch = s[i]
    i += 1
    num = ""
    while i < len(s) and s[i].isdigit():
        num += s[i]
        i += 1
    result += ch * int(num)
print("Decompressed:", result)