'''
Remove occurrences of a word. 
S = "a test b test c", 
Word = "test", 
Remove All "a b c"
'''

str = input("Enter String = ")
word = input("Enter Word = ")
words = str.split()

for ch in words:
    if  ch != word:
        print(ch,end = " ")
