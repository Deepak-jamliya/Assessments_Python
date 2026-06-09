'''
=====================================================================
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
'''

from collections import namedtuple

n = int(input("Enter Number of books = "))

books = namedtuple("books",["book_id", "title", "author", "price"])
data = []

for i in range(n):
    bid = input(f"Enter Book {i+1} id = ")
    t = input(f"Enter Book {i+1} title = ")
    a = input(f"Enter book {i+1} Author = ")
    p = int(input(f"Enter Book {i+1} Price = "))
    data.append(books(bid,t,a,p))

print("\nBook Details : ")
for i in data:
    print(i.book_id,i.title,i.author,i.price)

print("\nMost Expensive Book : ")
exp = data[0].price
name = data[0]
sum = 0
for i in data:
    if i.price > exp:
        exp = i.price
        name = i
    sum+=i.price
print(name.book_id,name.title,name.author,name.price)

au = input("Enter Author Name = ")

print(f"\nBooks Written By {au} : ")
for i in data:
    if i.author == au:
        print(i.book_id,i.title,i.author,i.price)

print("\nAverage Book Price : ")
print(sum/len(data))
