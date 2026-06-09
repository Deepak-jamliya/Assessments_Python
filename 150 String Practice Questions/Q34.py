'''
34Find the shortest word. 
S = "find the shortest word" 
"the"

'''
str = input("Enter string = ")

words = str.split()
smallest = len(words[0])
small = ""
i = 0
while i < len(words):
    if len(words[i]) <= smallest:
        smallest = len(words[i])
        small = words[i]
    i+=1
print(small)