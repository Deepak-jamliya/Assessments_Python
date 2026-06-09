'''
56Reverse only consonants. 
S = "apple" 
"eplpa"
'''

s = input("Enter String = ")

cons = []
for i in s:
    if i not in 'aeiou':
        cons.append(i)

result = ""
rev = cons[::-1]
c = 0

for i in s:
    if i in 'aeiou':
        result+=i
    else:
        result+=rev[c]
        c+=1
print(result)
