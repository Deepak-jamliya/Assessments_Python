'''
39Search all occurrences of a character. 
S = "banana", Char='a' 
1, 3, 5 (indices)
'''

str = input("Enter String = ")
char = input("Enter Character = ")

i = 0
while i < len(str):
    if str[i] == char:
        print(i,end = " ")
    i+=1
        
    