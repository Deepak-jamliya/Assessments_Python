'''
*
##
***
####
*****
'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()
    for j in range(i):
        if i%2 == 0:
            print("#",end = "")
        else:
            print("*",end = "")
            