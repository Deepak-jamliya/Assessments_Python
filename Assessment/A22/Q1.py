'''
1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels
 are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
'''

str = input("Enter feedback Message = ")
count = 0

for i in range(len(str)):
    ch = str[i]
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count+=1

print("Total Vowels = ",count)
