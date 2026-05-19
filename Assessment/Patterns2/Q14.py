'''
1
23
456
78910
'''
n = int(input("Enter n = "))

num = 1

for i in range(1, n + 1):
    print()
    j = 1
    while j <= i:
        print(num, end="")
        num += 1
        j += 1