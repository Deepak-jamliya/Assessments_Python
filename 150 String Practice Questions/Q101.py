'''
101Check if a string is a valid palindrome ignoring spaces and punctuation. 
S = "A man, a plan, a canal: Panama" 
TRUE

'''

s = input("Enter string = ")

clean = ""
for ch in s:
    if ch.isalpha():
        clean += ch.lower()

if clean == clean[::-1]:
    print("TRUE")
else:
    print("FALSE")