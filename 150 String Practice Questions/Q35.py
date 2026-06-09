'''
35Find the first palindrome word. 
S = "this madam is here" 
"madam"
'''

str = input("Enter String = ")

words = str.split()

for ch in words:
    if ch == ch[::-1]:
        print(ch)
        break