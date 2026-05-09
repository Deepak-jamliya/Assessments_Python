'''Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0
-----------------------------------------------------------------------------------------------------------------'''



dis,mil,pprice = map(int,input("Enter distance, mileage and petrol price(per litre) : ").split())



petrol = dis / mil

cost = petrol * pprice

print(f"Petrol USed = {petrol}\nTotal Cost = {cost}")