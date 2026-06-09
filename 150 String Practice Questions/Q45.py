'''
45Check whether a string starts with or ends with another string. 
S = "apple pie", Prefix = "apple", Suffix = "pie" 
Start: True, End: True
'''

str = input("Enter Str1 = ")
pre = input("Enter Prefix = ")
suf = input("Enter Suffix = ")

if str.startswith(pre) and str.endswith(suf):
    print("Start : ",True)
    print("End : ",True)
else:
    print("Start : ",False)
    print("End : ",False)
