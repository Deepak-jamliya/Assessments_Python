'''
48Remove all vowels. 
S = "aeiou XYZ" 
" XYZ"
'''

s = input("Enter String = ")

result = ""
for i in s:
    if i not in 'aeiou':
        result+=i

print(result)
