'''
 Count Even Digits*
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.

Input: 123456
Output: Even digits count = 3'''

# while loop
'''num = int(input("Number = "))
count = 0

while num > 0:
    digit = num % 10
    if digit %2 == 0:
        count+=1
    else:
        pass
    num = num // 10

print("Even digits count = ",count)'''


# for loop

num = int(input("Enter Number = "))
count = 0

for i in range(len(str(num))):
    digit = num % 10
    if digit%2 == 0:
        count+=1
    num = num // 10
print("Even Digits Count = ",count)