'''
96Find the second most frequent word. 
S = "a b a c b" 
c'
'''

S = input("Enter N = ")
words = S.split()

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

max_freq = 0
for word in counts:
    if counts[word] > max_freq:
        max_freq = counts[word]

second_freq = 0
for word in counts:
    if counts[word] > second_freq and counts[word] < max_freq:
        second_freq = counts[word]

result = ""
for word in counts:
    if counts[word] == second_freq:
        result = word
        break

print(result)