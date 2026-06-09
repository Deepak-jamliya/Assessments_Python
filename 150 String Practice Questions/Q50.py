'''
50Remove all digits. 
S = "a1b2c3" 
"abc"
'''

s = input("Enter String = ")

for i in s:
    if i.isalpha():
        print(i,end = "")