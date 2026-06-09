'''
88Rearrange a string so that identical characters are at least d distance apart. 
S = "aaabc", d = 2 
"abaca"

'''
s = input("Enter string = ")
d = int(input("Enter distance = "))

result = ""

for ch in s:
    if result == "":
        result += ch
    else:
        if result[-1] != ch:
            result += ch
        else:
            result = result[:-1] + ch + result[-1]

print(result)