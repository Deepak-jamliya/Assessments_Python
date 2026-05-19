'''
123456
54321
1234
321
12
1
'''

n = int(input("Enter n = "))

printasc = True 

for i in range(n, 0, -1):

    if printasc:
        for j in range(1, i + 1):
            print(j, end="")
        print()
        printasc = False

    else:
        for j in range(i, 0, -1):
            print(j, end="")
        print()
        printasc = True