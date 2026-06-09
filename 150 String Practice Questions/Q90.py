'''
90Remove adjacent duplicates recursively.
 S = "azxxzy" 
 "ay"

'''

s = input("Enter string = ")

while True:
    new = ""
    i = 0

    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i+1]:
            i += 2
        else:
            new += s[i]
            i += 1

    if new == s:
        break
    s = new

print(s)