'''
oggle the case of each character. 
S = "MiXED" 
"mIxeD"
'''
str = input("String = ")

new = ""
i = 0
while i < len(str):
    if str[i].isupper():
        new = new + str[i].lower()
    else:
        new = new + str[i].upper()
    i+=1

print(new)