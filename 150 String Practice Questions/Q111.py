'''
111Check if a string can be rearranged into a palindrome. 
S = "aabbc" 
TRUE

'''

s = input("Enter String = ")

odd = 0

for ch in s:
    if s.count(ch) % 2 != 0:
        odd += 1

print(odd <= 1)