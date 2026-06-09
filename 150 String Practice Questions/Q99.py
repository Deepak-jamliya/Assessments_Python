'''
99Check if a 'z' is happy (surrounded by same chars). 
S = "azzb" 
FALSE

'''

S = input("Enter String = ")

i = S.index('z')    
print(S[i-1] == S[i+1])