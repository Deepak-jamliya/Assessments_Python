'''
76Find the longest common suffix among strings. 
Strings = ["baking", "making", "taking"] 
"king"
'''

strings = ["baking", "making", "taking"]

shortest = min(strings, key=len)
suffix = ""

for i in range(1, len(shortest) + 1):
    match = True
    ch = shortest[-i]

    for s in strings:
        if s[-i] != ch:
            match = False
            break

    if not match:
        break

    suffix = ch + suffix

print(suffix)