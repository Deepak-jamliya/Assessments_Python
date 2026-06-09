'''
Print all characters that occur exactly twice. 
S = "aabbcdee" 
b', 'e'
'''

str = input("Enter string = ")

check = ""
for i  in str:
    count = 0
    for ch in str:
        if ch == i :
            count+=1
    if count == 2 and i not in check:
        check = check + i

print(check)

