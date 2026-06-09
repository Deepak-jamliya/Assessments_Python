'''
74Find the longest substring without repeating characters. 
S = "abcabcbb" 
"abc"
'''

s = input("Enter String = ")
longest = ""

for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        if s[j] not in temp:
            temp += s[j]
        else:
            break
    if len(temp) > len(longest):
        longest = temp

print(longest)