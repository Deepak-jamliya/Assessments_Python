'''
Find the highest frequency character. 
S = "abracadabra" 
a'
'''

str = input("Enter String = ")

hcount = 0
char = ""
for i in str:
    count = 0
    for j in str:
        if i == j:
            count+=1
    if count > hcount:
        hcount = count
        char = i
print(char)