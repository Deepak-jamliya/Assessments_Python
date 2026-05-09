tamount = int(input("Enter Total amount : ₹"))
ten = tamount//10
remain = tamount % 10
five = remain//5

print(f"Amount : {tamount}\nOutput : ₹10 x {ten}, ₹5 x {five}")