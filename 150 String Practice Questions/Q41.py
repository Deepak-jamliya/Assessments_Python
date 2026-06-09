'''
41Check if a string contains a substring (without using built-in method). 
S1 = "Hello", Sub="ell" 
TRUE
'''

s1 = input("Enter string = ")
sub = input("Enter Substring = ")

found = False
i = 0

while i <= len(s1) - len(sub):
    j = 0
    while j < len(sub):
        if s1[i + j] != sub[j]:
            break
        j += 1

    if j == len(sub):
        found = True
        break

    i += 1

if found:
    print("TRUE")
else:
    print("FALSE")