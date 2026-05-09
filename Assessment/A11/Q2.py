'''
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the
 scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2
'''

# while loop
'''num = int(input("Enter number : "))
smallest = 9

while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num = num // 10

print("Smallest Digit = ",smallest)'''

# for loop

num = int(input("Enter Number = "))
smallest = 9

for i in range(len(str(num))):
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num = num // 10

print("Smallest = ",smallest)
