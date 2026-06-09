'''
46Check if a substring appears at both the start and end. 
S = "abcabca", Sub = "abca" 
TRUE
'''


str = input("Enter Str1 = ")
sub = input("Enter Sub string = ")

if str.startswith(sub) and str.endswith(sub):
    print("Start : ",True)
    print("End : ",True)
else:
    print("Start : ",False)
    print("End : ",False)