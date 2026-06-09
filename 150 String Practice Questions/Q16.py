'''
Count total occurrences of a character. 
S = "programming", Char = 'g' 
2
'''
str,char = input("Enter String and char = ").split()

count = 0

for i in str:
    if i == char:
        count+=1

print(count)