'''
36Reverse order of words. 
S = "one two three" 
"three two one"
'''

str = input("Enter string = ")
words = str.split()

i = len(words) - 1
while i>=0:
    print(words[i],end = " ")
    i-=1