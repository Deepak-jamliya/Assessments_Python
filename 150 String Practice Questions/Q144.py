'''
144Check if a string is valid HTML/XML tag sequence. S = "<a><b></a></b>" FALSE

'''

s = "<a><b></b></a>"
stack = []
i = 0
valid = True
while i < len(s):
    if s[i] == "<":
        j = s.index(">", i)
        tag = s[i+1:j]
        if tag.startswith("/"):
            if not stack or stack[-1] != tag[1:]:
                valid = False
                break
            stack.pop()
        else:
            stack.append(tag)
        i = j + 1
    else:
        i += 1
if stack:
    valid = False
print("Valid HTML/XML:", valid)