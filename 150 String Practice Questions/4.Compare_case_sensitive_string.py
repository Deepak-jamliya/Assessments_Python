'''
Compare two strings (case-sensitive). 
S1 = "Test", S2 = "test" 
Not Equal (or non-zero value)
'''

s1,s2 = input("Enter S1 and S2 = ").split()

if s1 == s2:
    print("Equal Values")
else:
    print("Not Equal")