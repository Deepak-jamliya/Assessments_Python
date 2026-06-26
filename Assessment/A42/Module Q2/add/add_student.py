def add():
    name = input("Enter Student Name : ")
    roll = input("Enter Roll Number : ")
    marks = []
    for i in range(1, 6):
        mark = int(input(f"Enter Mark {i} : "))
        marks.append(mark)
    return name, roll, marks