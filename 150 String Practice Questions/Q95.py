'''
95Find the second most frequent character. 
S = "aabbccdde" 
c' or 'd'

'''

s = input("Enter string = ")

chars = ""
counts = []

for ch in s:
    if ch not in chars:
        chars += ch
        counts.append(s.count(ch))

max1 = max(counts)

max2 = 0
for c in counts:
    if c < max1 and c > max2:
        max2 = c

for i in range(len(chars)):
    if counts[i] == max2:
        print(chars[i])
        break