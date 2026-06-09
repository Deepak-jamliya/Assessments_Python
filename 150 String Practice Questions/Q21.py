'''
Find the first non-repeating character. 
S = "aabbcde" 
c'
'''
str = input("Enter String = ")

for i in str:
    count = 0
    for ch in str:
        if i == ch:
            count+=1
    if count == 1:
        print(i)
        break

