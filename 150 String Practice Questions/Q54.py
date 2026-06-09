'''
54Replace all duplicate characters with '$'. 
S = "hello" 
"he$lo"
'''

s = input("Enter String = ")

check = ""
result = ""

for i in s:
    if i in check:
        result+="$"
    else:
        check+=i
        result+=i
print(result)

        
