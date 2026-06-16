'''
8.
=========================================
LIBRARY BOOK ISSUE TRACKER
==========================

A library records issued books.

books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]

Write a program to:

* Count how many times each book was issued.

Sample Output:
{
'Python':3,
'Java':2,
'C++':1
}
'''

books = ["Python","Java","Python","C++","Java","Python"]

d = {}

for i in books:
    count = 0
    for j in books:
        if i == j:
            count+=1
    d[i] = count
print(d)

