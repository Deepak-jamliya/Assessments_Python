from add.add_student import add
from calculations import marks
from display import sheet




name = None
roll = None
marks = []
total = percentage = grade = None

while True:
    print("\nMenu")
    print("1. Add Student Details")
    print("2. Calculate Total Marks")
    print("3. Calculate Percentage")
    print("4. Find Grade")
    print("5. Display Complete Result")
    print("6. Find Highest Subject Mark")
    print("7. Find Lowest Subject Mark")
    print("8. Exit")

    choice = int(input("Enter Choice = "))

    match choice:
        case 1:
            name, roll, marks = add()

        case 2:
            total = marks.caltotal(marks)
            print("Total Marks:", total)

        case 3:
            percentage = marks.calpercentage(total)
            print("Percentage:", percentage)

        case 4:
            grade = marks.calgrade(percentage)
            print("Grade:", grade)

        case 5:
            sheet.display(name, roll, marks, total, percentage, grade)

        case 6:
            print("Highest Mark:", marks.highest(marks))

        case 7:
            print("Lowest Mark:", marks.lowest(marks))

        case 8:
            print("Thank You")
            break

        case _:
            print("Invalid Choice. Please try again.")