'''
100Return true if string contains 'abc' not followed by '.'. 
S1 = "abcx", S2 = "abc." 
S1: True, S2: False
'''

s = input("Enter string = ")

if "abc" in s and "abc." not in s:
    print("TRUE")
else:
    print("FALSE")