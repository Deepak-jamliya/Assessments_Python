'''
62Count vowels and consonants. 
S = "apple" 
Vowels: 2, Consonants: 3
'''

s = input("Enter String = ")

v = 0
c = 0
for i in s:
    if i in 'aeiou':
        v+=1
    else:
        c+=1

print("Vowels = ",v,"Consonants = ",c)