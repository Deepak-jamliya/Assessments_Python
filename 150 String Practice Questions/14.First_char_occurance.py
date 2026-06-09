'''
Find the first occurrence of a character. 
S = "banana", Char = 'a' 
1 (index)
'''

str,char = input("Enter String and char = ").split()

for i in range(len(str)):
    if str[i] == char:
        print(i)
        break