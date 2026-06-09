'''
Find the last occurrence of a character. 
S = "banana", Char = 'a' 
5 (index)
'''

str,char = input("Enter string and Char = ").split()

for i in range(len(str)-1,0,-1):
    if str[i] == char:
        print(i)
        break