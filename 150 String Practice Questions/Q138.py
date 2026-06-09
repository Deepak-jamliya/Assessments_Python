'''
138Find all palindromic partitions of a string. S = "aab" ["a", "a", "b"], ["aa", "b"]

'''

s = "aab"
result = []
n = len(s)
stack = [(0, [])]
while stack:
    start, path = stack.pop()
    if start == n:
        result.append(path)
        continue
    for end in range(start + 1, n + 1):
        sub = s[start:end]
        if sub == sub[::-1]:
            stack.append((end, path + [sub]))
print("Palindromic partitions:", result)