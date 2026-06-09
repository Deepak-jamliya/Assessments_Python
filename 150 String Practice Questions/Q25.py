'''
Count total words in a string. 
S = "This is a test" 
4
'''

str = input("Enter string = ")


'''
count = 1
i = 0
while i < len(str):
    if str[i] == " ":
        count+=1
    i+=1
print(count)'''


words = str.split()
print(len(words))
