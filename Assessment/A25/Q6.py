'''
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word 
appears in a review.

Input Sentence:

iphone is good and iphone battery is strong

Word:

iphone

Output:

2
'''

str = input("Enter Message = ")
word = input("Enter Word = ")
count = 0
words = str.split()

i = 0
while i < len(words):
    if words[i] == word:
        count+=1
    i+=1

print(count)