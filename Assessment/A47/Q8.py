class Member:
    def __init__(self,hoursWorkedOut):
        self.h=hoursWorkedOut
    def calculateRewardsPoints(self):
        print(self.h*2)
class PremiumMember(Member):
    def __init__(self,hoursWorkedOut):
        self.h=hoursWorkedOut
    def calculateRewardsPoints(self):
        print(self.h*4)

h=int(input("Enter the hours worked out"))

m=Member(h)
p=PremiumMember(h)

if input("The member is premium yes/no")=="yes":
    p.calculateRewardsPoints()
else:
    m.calculateRewardsPoints()