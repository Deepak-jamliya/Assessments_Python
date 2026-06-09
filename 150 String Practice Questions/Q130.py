'''
130Find the maximum occurring word. 
S = "a b a c a" 
a'

'''
s = "a b a c a"

words = s.split()

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

max_word = None
max_count = 0

for word, count in frequency.items():
    if count > max_count:
        max_count = count
        max_word = word

print(f"Max occurring word: '{max_word}' (appeared {max_count} times)")