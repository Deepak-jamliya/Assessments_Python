'''
6. Sum of Factors
A puzzle-based game rewards users based on the sum of all factors of a chosen number.
The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.

Input:
6

Output:
Sum = 12'''

# while loop
num = int(input("Enter Number = "))
sum = 0

i = 1
while i <= num:
    if num%i == 0:
        sum = sum + i
    i+=1
print("Sum = ",sum)

# for loop

'''num = int(input("Enter number : "))
sum = 0

for i in range(1,num+1):
    if num % i == 0:
        sum = sum + i

print("Sum = ",sum)'''