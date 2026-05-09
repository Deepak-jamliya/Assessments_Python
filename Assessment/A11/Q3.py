'''
3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID
 represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5'''

# while loop
'''num = int(input("Enter Number : "))

while num > 0:
    digit = num % 10
    num = num // 10

if num == 0:
        print("First digit : ",digit)'''

# for loop

num = int(input("Enter Number = "))

for i in range(len(str(num))):
    digit = num % 10
    num = num // 10
if num == 0:
    print("First Digit = ",digit)