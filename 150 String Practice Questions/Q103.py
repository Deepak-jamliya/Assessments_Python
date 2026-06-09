'''
103Check if a string contains balanced parentheses. 
S = "((()))" 
TRUE

'''

s = input("Enter string = ")

count = 0
balanced = True

for ch in s:
    if ch == '(':
        count += 1
    elif ch == ')':
        count -= 1

    if count < 0:
        balanced = False
        break

if balanced and count == 0:
    print("TRUE")
else:
    print("FALSE")