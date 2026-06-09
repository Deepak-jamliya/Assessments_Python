'''
149 Check if two strings are scrambled versions of each other.
S1 = "great", S2 = "rgeat"

'''

s1 = "great"
s2 = "rgeat"
sorted1 = sorted(s1)
sorted2 = sorted(s2)
print("Scrambled (same chars):", sorted1 == sorted2)