'''
3.

MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row 
represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45
'''


rows = int(input("Enter number of Employess = "))
cols = int(input("Enter Number of Months = "))
matrix = []


for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

while True:
    print("Menu")
    print("1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score")
    print("3. Display Employee-wise Maximum Score")
    print("4. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            largest = matrix[0][0]
            for i in range(rows):
                sum = 0
                for j in range(cols):
                    sum+=matrix[i][j]
                if sum > largest:
                    largest = sum
            print(f"Employee {i} has the highest total Score = ",largest)
        case 2:
            lowest = matrix[i][j]
            for j in range(cols):
                sum = 0
                avg = 0
                for i in range(rows):
                    sum+=matrix[i][j]
                avg = sum//len(matrix[j])
                print(f"Month {j+1} average = ",avg)
        case 3:
            for i in range(rows):
                largest = 0
                for j in range(cols):
                    if matrix[i][j] > largest:
                        largest = matrix[i][j]
                print(f"Employee {i+1} Max Score = ",largest)


                


