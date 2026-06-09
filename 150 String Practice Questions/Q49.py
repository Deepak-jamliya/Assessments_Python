'''
49Replace all consonants with ''. 
S = "apple" 
"ae"
'''

s = input("Enter String = ")

result = ""
for i in s:
    if i  in 'aeiou':
        result+=i
        

print(result)