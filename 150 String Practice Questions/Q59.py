'''
59Rotate characters by 3 positions to the right. 
S = "abcde" 
"cdeab"
'''

s = input("Enter String = ")

result = s[2:] + s[:2]
print(result)