'''
5) Number-Star Palindrome
    12344321
    123**321
    12****21
    1******1
'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()
    j = 1
    while j <= n-i+1:
        print(j,end = "")
        j+=1

    s = 1
    while s <= 2 * i - 2:
        print("*",end = "")
        s+=1

    k = n - i + 1
    while k >= 1:
        print(k,end = "")
        k-=1