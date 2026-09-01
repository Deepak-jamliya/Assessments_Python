class Customer:
    def __init__(self,amount_spend):
        self.amount_sepnd=amount_spend
        print("Loyality points = ",amount_spend/10)

class Premiuncustomer:
    def __init__(self,amount_spend):
        self.amount_spend=amount_spend
        print("loyality points = " ,2* amount_spend / 10  )

amount_spend=int(input("enter amount spend")) 
status=input("enter ststus")

if status=="yes":
    Premiuncustomer(amount_spend)
else:
    Customer(amount_spend)