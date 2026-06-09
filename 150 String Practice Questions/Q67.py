'''
67Count how many times a substring appears. 
S = "abab", Sub = "ab" 
2
'''

s = input("Enter String = ")
sub = input("Enter SUbstring = ")
count = 0

i = 0
while i <= len(s) - len(sub):
    j = 0
    match = 1
    while j < len(sub):
        if s[i+j] != s[j]:
            match = 0
            break
        j+=1
    if match:
        count+=1
    i+=1
print(count)
