'''
125Find the shortest common supersequence of two strings. 
S1 = "AGGTAB", S2 = "GXTXAYB" 
"AGGXTXAYB"

'''

s1 = "AGGTAB"
s2 = "GXTXAYB"

i = j = 0
scs = ""

while i < len(s1) and j < len(s2):
    if s1[i] == s2[j]:
        scs += s1[i]
        i += 1
        j += 1
    elif s1[i] in s2[j:]:
        scs += s2[j]
        j += 1
    else:
        scs += s1[i]
        i += 1

scs += s1[i:] + s2[j:]
print(scs)