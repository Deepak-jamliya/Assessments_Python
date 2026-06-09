'''
3.
=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2
'''

rows = int(input("Enter Number of rows = "))
cols = int(input("Enter Number of Columns = "))

matrix = []
print("Enter Elements of Matrix 1")
for i in range(rows):
   row = []
   for j in range(cols):
      row.append(int(input()))
   matrix.append(row)

while True:
    print("Menu")
    print("1. Count Armstrong Numbers Row-wise")
    print("2. Count Palindrome Numbers Column-wise")
    print("3. Display Average of Each Row")
    print("4. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            for i in range(rows):
                count = 0
                for j in range(cols):
                    sum = 0
                    num = matrix[i][j]
                    check = num
                    power = len(str(num))
                    while num > 0:
                        digit = num % 10
                        sum = sum + digit**power
                        num = num // 10
                    if sum == check:
                        count+=1
                print(f"Row {i+1} Armstrong Count = ",count)
        case 2:
            for j in range(cols):
                count = 0
                for i in range(rows):
                    num = matrix[i][j]
                    check = num
                    rev = 0
                    while num > 0:
                        digit = num % 10
                        rev = rev * 10 + digit
                        num = num // 10

                    if check == rev:
                        count+=1
                print(f"Column {i+1} Palindrome Count = ",count)
        case 3:
            for i in range(rows):
                avg = 0
                sum = 0
                for j in range(cols):
                    sum+=matrix[i][j]
                avg = sum / len(rows)

                print(f"Row {i+1} average = ",avg)
        case 4:
            print("Thank You for Using Matrix Analysis System")
            break 
        case _:
            print("Invalid Choice")

                    


                  



   