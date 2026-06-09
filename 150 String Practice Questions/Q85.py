'''
85Convert string into a char array without built-in functions. 
S = "test" 
{'t', 'e', 's', 't'}
'''

s = input("Enter String = ")

array = []

for ch in s:
    array.append(ch)

print(array)