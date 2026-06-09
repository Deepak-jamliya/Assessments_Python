'''
87Print all permutations of a string with repetition. 
S = "aab" 
"aab", "aba", "baa"

'''

s = input("Enter string = ")

printed = ""

for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i != j and j != k and i != k:
                word = s[i] + s[j] + s[k]
                if word not in printed:
                    print(word)
                    printed += word + " "