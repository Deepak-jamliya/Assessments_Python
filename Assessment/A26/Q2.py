'''
2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated 
keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india
'''

str = input("Enter string = ")
words = str.split()

highest = 0
hchar = ""

for i in words:
    count = 0
    for ch in words:
        if i == ch:
            count+=1
    if count > highest:
        highest = count
        hchar = i

print(hchar)