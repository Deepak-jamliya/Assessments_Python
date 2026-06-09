'''
# 3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat 
in the transaction ID.

If no unique digit exists, print:

text
No unique digit found

### Input:
text
A122334455667789

### Output:

text
8
'''

str = input("Enter String = ")

f = 1
i = 0
while i < len(str):
    ch = str[i]
    if ch.isdigit():
        count = 0
        j = 0
        while j < len(str):
            if str[j] == ch:
                count+=1
            j+=1
        if count == 1:
            print(ch)
            f = 0
            break
    i+=1
    
if f:
    print("No Unique Digit Found")