'''
127Group words that are anagrams from an array of strings. 
Arr = ["eat", "tea", "tan", "ate", "nat"]
 [["eat", "tea", "ate"], ["tan", "nat"]]

'''

arr = ["eat", "tea", "tan", "ate", "nat"]
result = []
used = [False] * len(arr)

for i in range(len(arr)):
    if used[i]:
        continue

    group = [arr[i]]
    used[i] = True

    for j in range(i + 1, len(arr)):
        if not used[j] and sorted(arr[i]) == sorted(arr[j]):
            group.append(arr[j])
            used[j] = True

    result.append(group)

print(result)