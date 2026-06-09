'''
Find the length of a string. 
S = "programming" 
11
'''

str = input("Enter String = ")

count = 0
i = 0
while i < len(str):
    count+=1
    i+=1

print(count)
print(len(str))