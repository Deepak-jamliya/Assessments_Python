'''
Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3
'''

num = int(input("Enter number : "))
num1 = int(input("Enter digit : "))
count = 0

# while loop
'''while num > 0:
    digit = num % 10
    if digit == num1:
        count+=1
    else:
        pass
    num = num // 10

print(count)'''

# for loop

for i in range(len(str(num))):
    digit = num % 10
    if digit == num1:
        count+=1
    num = num // 10

print(count)