'''
75Find the longest common prefix among strings. 
Strings = ["flower", "flow", "flight"] 
"fl"

'''
strings = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(strings[0])):
    ch = strings[0][i]
    for s in strings:
        if i >= len(s) or s[i] != ch:
            print(prefix)
            exit()
    prefix += ch

print(prefix)
