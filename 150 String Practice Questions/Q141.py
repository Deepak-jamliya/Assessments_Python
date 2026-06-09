'''
141 Implement Rabin-Karp algorithm for substring search. Text = "abcxabc", Pattern = "abc" 0, 4 (indices)

'''

text = "abcxabc"
pattern = "abc"
n = len(text)
m = len(pattern)
base = 26
mod = 101
p_hash = 0
t_hash = 0
h = 1
indices = []
for i in range(m - 1):
    h = (h * base) % mod
for i in range(m):
    p_hash = (base * p_hash + ord(pattern[i])) % mod
    t_hash = (base * t_hash + ord(text[i])) % mod
for i in range(n - m + 1):
    if p_hash == t_hash:
        if text[i:i+m] == pattern:
            indices.append(i)
    if i < n - m:
        t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
        if t_hash < 0:
            t_hash += mod
print("Rabin-Karp found at indices:", indices)