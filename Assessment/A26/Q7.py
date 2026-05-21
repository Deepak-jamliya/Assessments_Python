'''
7.
Customer Feedback Analysis System

An e-commerce company receives thousands of customer reviews every day for its products.

To analyze customer opinions efficiently, the analytics team wants a Python program that counts 
how many times each word appears in a review message.

This helps the company identify frequently used words such as:

good
bad
delivery
quality
service

Write a Python program to count the frequency of every word in a given sentence.

Input:
delivery was fast and delivery service was good
Output:
delivery : 2
was : 2
fast : 1
and : 1
service : 1
good : 1
'''

str = input("Enter String = ")

words = str.split()

i = 0
while i < len(words):
    count = 0
    seen = False
    k = 0
    while k < i:
        if words[i] == words[k]:
            seen = True
            break
        k += 1
    if seen == False:
        j = 0
        while j < len(words):
            if words[i] == words[j]:
               count+=1
            j+=1
        print(words[i] ," : ",count )
      
    i+=1