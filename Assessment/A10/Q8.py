''' Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3'''

# while loop

'''num = int(input("Enter Number : "))
count = 0

while num > 0:
    digit = num % 10
    if digit %2 != 0:
        count+=1
    else:
        pass
    num = num // 10

print("Odd digits count = ",count)'''

# for loop

num = int(input("Enter Number = "))
count = 0

for i in range(len(str(num))):
    digit = num % 10
    if digit%2 != 0:
        count+=1
    num = num // 10
print("Odd digit Count = ",count)
