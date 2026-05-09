'''
7. Power of a Number
A scientific calculator app is used by engineering students for repeated
multiplication operations. It should calculate the value of a number raised 
to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32'''

# while loop
n,p = map(int,input("Enter Number and its power : ").split())
multiply = 1
i = 1
while i <= p:
    multiply = multiply * n
    i+=1
print(multiply)

# for loop
'''a,b = map(int,input("Enter num and power : ").split())
multiply = 1

for i in range(1,b+1):
    multiply = multiply * a

print(multiply)'''

