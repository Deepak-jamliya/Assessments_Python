'''
Get the Unicode code point before index. 
S = "Hello", Index = 1 
72 (Unicode for 'H')
'''

str = input("Enter String = ")
index = int(input("Enter Index = "))

print(ord(str[index-1]))