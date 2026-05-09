'''
3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35
'''

a,b = map(int,input("Enter 2 numbers : ").split())

for i in range(a,b):
    if i%10 == 5:
        print(i,end = " ")