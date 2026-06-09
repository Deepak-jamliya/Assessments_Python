'''
79Divide a string into n equal parts. 
S = "abcdef", n = 3 
"ab", "cd", "ef"
'''
s = input("Enter String = ")
n = 3

length = len(s)

if length % n != 0:
    print("Cannot divide into equal parts")
else:
    size = length // n
    parts = []

    for i in range(0, length, size):
        parts.append(s[i:i+size])

    print(", ".join(parts))