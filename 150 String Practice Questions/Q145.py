'''
145Remove HTML tags from a string. S = "<h1>Title</h1>" "Title"

'''

s = "<h1>Title</h1>"
result = ""
inside_tag = False
for ch in s:
    if ch == "<":
        inside_tag = True
    elif ch == ">":
        inside_tag = False
    elif not inside_tag:
        result += ch
print("Without HTML tags:", result)