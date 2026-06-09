'''
53Remove all punctuation characters. 
S = "Hello, world!" 
"Hello world"
'''

s = input("Enter String = ")

for i in s:
    if i not in '!,:.;':
        print(i,end = "")