'''
5.
====================================================================
 Student Classroom Matrix Analysis
====================================================================

Scenario

A school stores student marks in a matrix.

Rows represent different classrooms.
Columns represent students in each classroom.

The principal wants to analyze the performance of each classroom by
calculating the total marks scored by students in every row.

Requirements

* Read number of rows from user
* Read number of columns from user
* Read all matrix elements from user
* Display the complete matrix
* Find Row Wise Sum
* Display sum of each row separately

Test Case 1

Input:

Rows = 3
Columns = 3

Matrix:

10 20 30
40 50 60
70 80 90

Output:

Matrix:

10 20 30
40 50 60
70 80 90

Row 1 Sum = 60
Row 2 Sum = 150
Row 3 Sum = 240

------------------------------------------------------------

Test Case 2

Input:

Rows = 2
Columns = 4

Matrix:

1 2 3 4
5 6 7 8

Output:

Matrix:

1 2 3 4
5 6 7 8

Row 1 Sum = 10
Row 2 Sum = 26

------------------------------------------------------------

Test Case 3

Input:

Rows = 2
Columns = 2

Matrix:

100 200
300 400

Output:

Matrix:

100 200
300 400

Row 1 Sum = 300
Row 2 Sum = 700

------------------------------------------------------------

Additional Challenge

Also Display:

* Row Wise Sum
* Row Wise Average
* Row Having Maximum Sum
* Grand Total of Matrix

Sample Output

===== MATRIX REPORT =====

Matrix:

10 20 30
40 50 60
70 80 90

Row 1 Sum = 60
Row 2 Sum = 150
Row 3 Sum = 240

Row 1 Average = 20.0
Row 2 Average = 50.0
Row 3 Average = 80.0

Maximum Sum Row = Row 3
Grand Total = 450
'''

r = int(input("Enter Number of rows = "))
c = int(input("Enter Number of columns = "))

matrix = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter Value = ")))
    matrix.append(row)

maxrow = 0
max = 0
total = 0
for i in range(len(matrix)):
    sum = 0
    for j in range(len(matrix[i])):
        sum+=matrix[i][j]
        total+=matrix[i][j]
    avg = sum/len(matrix[i])
    if sum > max:
        max = sum
        maxrow = i+1
    print(f"Row {i+1} Sum = ",sum)

for i in range(len(matrix)):
    sum = 0
    for j in range(len(matrix[i])):
        sum+=matrix[i][j]
    avg = sum/len(matrix[i])
    print(f"Row {i+1} Average = ",avg)

print("Maximum Sum Row = Row",maxrow)
print("Grand Total = ",total)

