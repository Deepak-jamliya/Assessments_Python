'''
8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose token numbers are multiples of 5.
The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.

Input:
1 20

Output:
Count = 4'''

# while loop
a,b = map(int,input("Enter any two Numbers = ").split())
count = 0

while a <= b:
    if a%5 == 0:
        count+=1
    a+=1
print("Count = ",count)


# for loop
'''a,b = map(int,input("Enter range : ").split())
count = 0

for i in range(a,b+1):
    if i%5 == 0:
        count+=1

print("Count = ",count)'''