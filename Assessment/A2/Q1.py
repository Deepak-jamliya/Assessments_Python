total = int(input("Enter the total duration in seconds : "))
hrs = total//3600
remain = total % 3600

min = remain//60
sec = remain % 60

print(f"Hours : {hrs}, Minutes : {min}, seconds : {sec}")