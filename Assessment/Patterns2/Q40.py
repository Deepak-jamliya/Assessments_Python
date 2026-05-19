'''
*
**
****
*******
***********
'''

n = int(input("Enter n = "))

stars = 1   

for i in range(1, n + 1):
    print("*" * stars)
    stars = stars + i