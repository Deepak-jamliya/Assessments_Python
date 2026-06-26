def display(name, roll, marks, total, percentage, grade):
    print("\n----------- RESULT CARD -----------")
    print(f"Name        : {name}")
    print(f"Roll Number : {roll}")
    print("\nMarks")
    for i in range(5):
        print(f"Subject {i+1} : {marks[i]}")
    print(f"\nTotal Marks : {total}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")