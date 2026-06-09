'''
126Print all anagrams of a string. 
S = "cat" 
"cat, cta, act, atc, tca, tac"

'''

s = "cat"

for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i != j and j != k and i != k:
                print(s[i] + s[j] + s[k], end=", ")