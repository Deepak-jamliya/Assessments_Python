'''
52Remove all special characters. 
S = "a!@b#c" 
"abc"
'''

s = input("Enter String = ")

for i in s:
    if i not in '!@#$%^&*':
        print(i,end = "")