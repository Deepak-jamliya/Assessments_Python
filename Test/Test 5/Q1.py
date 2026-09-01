s = input("Enter String = ")

for i in range(len(s) - 1, 0, -1):
    same = True
    for j in range(i):
        if s[j] != s[len(s) - i + j]:
            same = False
            break

    if same:
        print(s[:i])
        break
else:
    print("Not Found")