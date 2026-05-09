'''
2. Factorial of a Number
In project scheduling, tasks are dependent on previous tasks,
and the total number of ways to arrange them is calculated 
using factorial. Factorial of a number n is the product of 
all numbers from 1 to n.
Write a program to calculate the *factorial of a given number
using loops*.

Input: n = 5
Output: Total Ways = 120
'''

num = int(input("Enter N = "))

# while loop
factor = 1
i = 1
while i <= num:
    factor = factor * i
    i+=1
print("Total Ways = ",factor)


#for loop
'''factor = 1
for i in range(num,1,-1):
    factor = factor * i

print("Total Ways : ",factor)'''




