'''
Count occurrences of a word. 
S = "word word other word", 
Word = "word" 
3
'''

str = input("Enter string = ")
word = input("Enter Word = ")

words = str.split()

count = 0
for i in words:
    if word == i:
        count+=1

print(count)