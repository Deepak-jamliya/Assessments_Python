'''
4.
=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal
'''

rows = int(input("Enter Number of rows = "))
cols = int(input("Enter Number of columns = "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input("Enter Element = ")))
    matrix.append(row)


while True:
    print("\nMenu")
    print("1. Display Main Diagonal Elements")
    print("2. Display Secondary Diagonal Elements")
    print("3. Compare Main and Secondary Diagonal Sums")
    print("4. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            print("Main Diagonal Elements : ")
            for i in range(rows):
                for j in range(cols):
                    if i == j:
                        print(matrix[i][j],end = " ")

        case 2:
            print("Secondary Diagonal Elements : ")
            for i in range(rows):
                for j in range(cols):
                    if i+j == rows - 1:
                        print(matrix[i][j],end = " ")
        
        case 3:
            msum = 0
            for i in range(rows):
                for j in range(cols):
                    if i == j:
                        msum+=matrix[i][j]
            print("Main Diagonal Sum = ",msum)
            
            ssum = 0
            for i in range(rows):
                for j in range(cols):
                    if i+j == rows - 1:
                        ssum+=matrix[i][j]
            print("Secondary Diagonal Sum = ",ssum)

            if msum > ssum:
                print("Main Diagonal Sum is Greater")
            elif msum == ssum:
                print("Both Sum is Equal")
            else:
                print("Seccondary Diagonal Sum is Greater")

        case 4:
            print("Thank You for Using Matrix Diagonal Analysis System")
            break
        case _:
            print("Invalid Choice")