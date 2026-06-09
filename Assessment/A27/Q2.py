'''
# 2. AI Auto-Correct Consecutive Word Remover

An AI-powered typing assistant often captures duplicate consecutive words while converting speech 
into text.

The company wants a Python program that removes only consecutive duplicate words while 
preserving the original sentence structure.

### Input:

text
hello hello hello team meeting meeting started


### Output:

text
hello team meeting started
'''

str = input("Enter String = ")
words = str.split()

new = ""
i = 0
while i < len(words):
    ch = words[i]
    if ch not in new:
        new = new +" "+ ch
    i+=1

print(new)
        