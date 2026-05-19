'''
28) Hollow Square
    *****
    *   *
    *   *
    *   *
    *****
'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()
    for j in range(1,n+1):
        if i == 1 or i == n:
            print("*",end = "")

        else:
            