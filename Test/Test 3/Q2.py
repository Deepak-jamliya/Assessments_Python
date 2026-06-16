'''2.   3.5 marks

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)'''




from collections import namedtuple

n = int(input("Enter Number of Players = "))
players = namedtuple("players",["player_id", "player_name", "runs_scored"])
data = []

for i in range(n):
    id = int(input(f"Enter ID of Player {i+1} = "))
    name = input(f"Enter Name of Player {i+1} = ")
    runs = int(input(f"Enter Runs Scored By Player {i+1} = "))
    data.append(players(id,name,runs))

for i in data:
    print(i.player_id,i.player_name,i.runs_scored)

highest = data[0]
lowest = data[0]
sum = 0

for p in data:
    if p.runs_scored > highest.runs_scored:
        highest = p
    if p.runs_scored < lowest.runs_scored:
        lowest = p
    sum+=p.runs_scored



print("Highest Runs Scored by = ",tuple(highest))
print("Lowest Runs Scored By = ",tuple(lowest))
print("Total Runs = ",sum)
print("Average Runs = ",sum/n)

for p in data:
    if p.runs_scored > 50:
        print(p.player_id,p.player_name,p.runs_scored)

