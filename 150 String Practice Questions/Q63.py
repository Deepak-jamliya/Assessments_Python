'''
63Count frequency of each character. 
S = "aabcc" 
a: 2, b: 1, c: 2
'''

s = input("Enter String = ")

check = ""

for i in s:
    count = 0
    if i not in check:
        for ch in s:
            if i == ch:
                count+=1
            check+=i
        print(i," : ",count)

        