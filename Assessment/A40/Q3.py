'''
3.
Cricket Tournament – Highest Run Scorer

A cricket academy wants to reward the player who scored the highest number of runs in a tournament.

Write a Python program to identify the highest run scorer using reduce() and a lambda expression.

Input
players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]
Expected Output
Highest Run Scorer: Rohit
'''

from functools import reduce
def main():
    n = int(input("Enter Number of Players = "))
    players = []

    for i in range(n):
        name = input(f"Enter Player {i+1} name = ")
        runs = int(input(f"Enter Player {i+1} runs = "))
        players.append((name,runs))

    result = reduce(lambda x,y: x if x[1] > y[1] else y,players)
    return result[0]

print(main())