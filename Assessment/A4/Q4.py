'''Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
------------------------------------------------------------------------------------'''


S = int(input("Enter speed : "))
hrs,min = map(int,input("Enter Hours and minutes : ").split())

totalt = hrs + (min/60)

Dis = S*totalt

print(f"Total Time = {totalt} hours\nDistance = {Dis}Km")



