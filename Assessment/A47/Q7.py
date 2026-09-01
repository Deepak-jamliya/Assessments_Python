class Pizza:
    def __init__(self,base_price,topping_cost,no_of_toppings):
        self.b=base_price
        self.t=topping_cost
        self.n=no_of_toppings

    def calculate_price(self):
        c=self.b+(self.t*self.n)
        print("Price without discount:",c)



class DiscountedPizza(Pizza):
     def __init__(self,base_price,topping_cost,no_of_toppings):
         super().__init__(base_price,topping_cost,no_of_toppings)

     def calculate_price(self):
         c=(self.b+(self.t*self.n))-(10/100)*(self.b+(self.t*self.n))
         print("Price with discount:",c)

b=float(input("Enter the base price"))
t=float(input("Enter the topping cost"))
n=float(input("Enter the number of toppings"))


a=Pizza(b,t,n)
a.calculate_price()

b=DiscountedPizza(b,t,n)

if n>3:
    
    b.calculate_price()
else:
    a.calculate_price()