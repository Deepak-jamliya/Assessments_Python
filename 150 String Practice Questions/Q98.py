'''
98Check if the first 'z' is immediately followed by another 'z'. 
S1 = "zzyy", S2 = "zyzz" 
S1: True, S2: False

'''

S1 = input("Enter String = ")
S2 = input("Enter String = ")

i = S1.index('z')
print(S1[i+1] == 'z')

i = S2.index('z')
print(S2[i+1] == 'z')