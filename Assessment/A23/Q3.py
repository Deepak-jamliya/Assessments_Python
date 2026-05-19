'''
3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5
'''

msg = input("Enter complaint = ")

words = msg.split()

count = 0

for w in words:
    count+=1

print("Total Words = ",count)