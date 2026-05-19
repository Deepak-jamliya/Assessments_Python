'''
*****
*****
*****
*****
*****
'''

n = int(input("Enter n = "))
'''
for i in range(n):
    print()
    for j in range(n):
        print("*",end = "")'''

i = 1
while i<=n:
    print()
    j = 1
    while j<=n:
        print("*",end = "")
        j+=1
    i+=1
