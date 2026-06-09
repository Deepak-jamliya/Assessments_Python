'''

# 5. Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique 
characters from a hashtag.

### Input:

text
aabcbcdbca

### Output:
text
dbca

### Explanation:

dbca contains all unique characters: a,b,c,d
'''

str = input("Enter string = ")

prev = ""
i = 0
while i < len(str):
    new = ""
    j = 0
    while j < len(str):
        if str[i] not in new:
            new = new + str[i]
        j+=1
    if len(new) > len(prev):
        prev = new
    i+=1
print(prev)