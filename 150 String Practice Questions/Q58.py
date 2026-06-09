'''
58Rotate characters by 2 positions to the left. 
S = "abcde" 
"cdeab"
'''

s = input("Enter String = ")

result = ""

i = 2
while i < len(s):
    result+=s[i]
    i+=1

result+=s[:2]

print(result)

# result = s[2:] + s[:2]