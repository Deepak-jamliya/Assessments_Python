'''
33Find the longest word. 
S = "find the longest word" 
"longest"
'''

str = input("Enter string = ")

words = str.split()

longest = len(words[0])
ans = ""
i = 0
while i < len(words):
    if len(words[i]) > longest:
        longest = len(words[i])
        ans = words[i]
    i+=1

print(ans)
