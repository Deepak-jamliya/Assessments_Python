'''
128Check if a string follows a given pattern. 
Pattern = "abba", 
S = "dog cat cat dog" 
TRUE

'''

pattern = "abba"
s = "dog cat cat dog"

word = ""
words = ""
count = 0
valid = True

for ch in s + " ":
    if ch != " ":
        word += ch
    else:
        words += word + ","
        word = ""
        count += 1

if count != len(pattern):
    valid = False
else:
    i = 0
    while i < len(pattern):
        j = i + 1
        while j < len(pattern):
            if pattern[i] == pattern[j]:
                if words.split(",")[i] != words.split(",")[j]:
                    valid = False
            else:
                if words.split(",")[i] == words.split(",")[j]:
                    valid = False
            j += 1
        i += 1

print(valid)