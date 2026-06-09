'''
82Create a string from a character array. 
Char[] = {'h', 'i'} 
"hi"
'''


chars = list(input("Enter Characters = ").split())
result = ""

for ch in chars:
    result = result + ch

print(result)