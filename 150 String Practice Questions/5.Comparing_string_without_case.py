'''
Compare two strings ignoring case. 
S1 = "Test", S2 = "test" 
Equal (or 0)
'''

s1,s2 = input("Enter s1 and s2 = ").lower().split()

if s1 == s2:
    print("Equal Values")
else:
    print("Not Equal")