'''
91Check if two strings are interleaving of another string. 
S1 = "aab", S2 = "axy", S3 = "aaxaby" 
TRUE
'''

s1 = input()
s2 = input()
s3 = input()

for ch in s1:
    s3 = s3.replace(ch, '', 1)

for ch in s2:
    s3 = s3.replace(ch, '', 1)

if s3 == "":
    print("TRUE")
else:
    print("FALSE")