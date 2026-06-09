'''
61Count total alphabets, digits, and special characters. 
S = "a1b!c2" 
Alphabets: 3, Digits: 2, Special: 1
'''

s = input("Enter String = ")

alpha = 0
digit = 0
special = 0

for i in s:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        alpha+=1
    else:
        special+=1

print("Alphabets: ",alpha," Digits: ",digit," Special: ",special)