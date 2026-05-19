'''
1
222
33333
4444444
555555555
'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()
    for j in range(1,(i*2-1)+1):
        print(i,end = "")