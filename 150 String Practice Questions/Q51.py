'''
51Extract only digits. 
S = "a1b2c3" 
"123"

'''

s = input("Enter String = ")

for i in s:
    if i.isdigit():
        print(i,end = "")