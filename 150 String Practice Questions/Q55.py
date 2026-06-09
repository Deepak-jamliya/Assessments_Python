'''
55Reverse only vowels. 
S = "hello" 
"holle"
'''

s = input("Enter String = ")

vowels = []
for i in s:
    if i in 'aeiou':
        vowels.append(i)

rev = vowels[::-1]
result = ""

j = 0
for i in s:
    if i in 'aeiou':
        result+= rev[j]
        j+=1
    else:
        result+=i
print(result)