'''
80Print list items containing all characters of a given word. 
List = ["apple", "plea"], Word = "pal" 
"apple", "plea"
'''

lst = ["apple", "plea"]
word = "pal"

for item in lst:
    found = True
    for ch in word:
        if ch not in item:
            found = False
            break
    if found:
        print(item)