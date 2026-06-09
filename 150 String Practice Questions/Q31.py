'''
Remove duplicate words. 
S = "the cat and the dog" 
"the cat and dog"
'''

str = input("Enter String = ")
words = str.split()

new = ""
for i in words:
    if i not in new:
        new = new + " " + i
print(new)