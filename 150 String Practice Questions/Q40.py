'''
40Search all occurrences of a word. 
S = "a b a b", Word='b' 
2, 6 (start indices)
'''

str = input("Enter String = ")
char = input("Enter Character = ")

i = 0
while i < len(str):
    if str[i] == char:
        print(i,end = " ")
    i+=1
        