'''
37Reverse each word. 
S = "cat dog" 
"tac god"
'''

str = input("Enter string = ")

words = str.split()

for ch in words:
    print(ch[::-1],end = " ")