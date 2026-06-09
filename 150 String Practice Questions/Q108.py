'''
108Check if a string is an isogram (no repeating letters). 
S = "ambidextrous" 
TRUE
'''

s = input("Enter String = ")

flag = 0
check = ""

for i in s:
    if i not in check:
        check+=i
    else:
        flag = 1
        break
if flag == 0:
    print(True)
else:
    print(False)