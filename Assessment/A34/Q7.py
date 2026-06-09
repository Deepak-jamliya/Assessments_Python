'''
7.

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
(105, 'SKY', 76)
'''

from collections import namedtuple

n = int(input("Enter Number of Players = "))
player = namedtuple("player",["player_id", "player_name", "runs_scored"])

data = []

for i in range(n):
    pid = int(input(f"Enter Player {i+1} id = "))
    name = input(f"Enter Player {i+1} Name = ")
    runs = int(input(f"Enter Runs Scored by Player {i+1} = "))
    data.append(player(pid,name,runs))

print("\nAll Players : ")
for i in data:
    print(i.player_id,i.player_name,i.runs_scored)

highest = data[0].runs_scored
high = data[0]
lowest = data[0].runs_scored
low = data[0]
sum = 0

for i in data:
    if i.runs_scored > highest:
        highest = i.runs_scored
        high = i
    if i.runs_scored < lowest:
        lowest = i.runs_scored
        low = i
    sum+=i.runs_scored

    
print("\nHighest Scorer")
print(high.player_id,high.player_name,high.runs_scored)

print("\nLowest Scorer : ")
print(low.player_id,low.player_name,low.runs_scored)

print("\nTotal Runs : ")
print(sum)

print("\nAverage Runs : ")
print(sum/len(data))

print("\nPlayers Scoring More Than 50 Runs : ")
for i in data:
    if i.runs_scored > 50:
        print(i.player_id,i.player_name,i.runs_scored)


    
