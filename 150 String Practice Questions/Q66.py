'''
66Count number of sentences in a paragraph. 
P = "This. Is. Test." 
3
'''

s = input("Enter paragraph = ")

count = 0
for i in s:
    if i == ".":
        count+=1
print(count)