'''
117Check if a string contains duplicate substrings. 
S = "ababa" 
True (e.g., "aba")

'''

s = input("Enter String = ")

found = False

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        sub = s[i:j]
        if sub and s.count(sub) > 1:
            found = True
            break
    if found:
        break

print(found)