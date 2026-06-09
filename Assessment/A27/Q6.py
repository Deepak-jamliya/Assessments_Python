'''
# 6. AI Chat Toxic Pattern Detector

An AI moderation system wants to detect whether a sentence contains three consecutive repeating 
characters.

If found:

text
Spam Pattern Found

Else:

text
Clean Message

### Input:

text
heyyy broooo welcome

### Output:

text
Spam Pattern Found
'''

text = input("Enter string = ")

spam = False

for i in range(len(text) - 2):
    if text[i] == text[i+1] == text[i+2]:
        spam = True
        break

if spam:
    print("Spam Pattern Found")
else:
    print("Clean Message")
