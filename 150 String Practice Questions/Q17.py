'''
Remove occurrences of a character. 
S = "banana", Char = 'a', 
Remove All "bnn"
'''

str,char = input("Enter String and Char = ").split()

new = ""
for i in str:
    if i != char:
        new = new + i

print(new)