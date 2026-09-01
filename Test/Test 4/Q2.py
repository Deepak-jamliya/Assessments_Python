'''problem 2:-   3 marks

Matrix Multiplication

Write a Python program to read two matrices from the user and perform matrix multiplication.

Before multiplying the matrices, check whether multiplication is possible. Matrix multiplication is possible only if
the number of columns in the first matrix is equal to the number of rows in the second matrix.

Requirements
Read the number of rows and columns for the first matrix.
Read all the elements of the first matrix from the user.
Read the number of rows and columns for the second matrix.
Read all the elements of the second matrix from the user.
Check whether matrix multiplication is possible.
If possible, multiply the matrices using nested loops.
Display the resulting matrix.

If multiplication is not possible, display:

Matrix multiplication is not possible.'''

r1 = int(input("Enter R1 = "))
c1 = int(input("Enter C1 = "))

r2 = int(input("Enter R2 = "))
c2 = int(input("Enter C2 = "))


print("Enter Elements of matrix 1 : ")
matrix1 = []
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    matrix1.append(row)

print("Enter Elements of matrix 2 : ")
matrix2 = []
for i in range(r2):
    row = []
    for j in range(c2):
        row.append(int(input()))
    matrix2.append(row)

if c1 != r2:
    print("Multiplication Not Possible")

else:
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            row.append(0)
        result.append(row)

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]

    print("Matrix 3")
    for i in result:
        print(i)

