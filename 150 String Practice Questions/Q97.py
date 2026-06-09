'''
97Check if two given strings appear at the end of each other (ignoring case). 
S1 = "abc", S2 = "Xabc" 
TRUE

'''
S1 = input("Enter String = ")
S2 = input("Enter String = ")

S1 = S1.lower()
S2 = S2.lower()

if S1.endswith(S2) or S2.endswith(S1):
    print("TRUE")
else:
    print("FALSE")