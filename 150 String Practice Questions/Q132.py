'''
132Check if a string is a valid IP address. S = "192.168.1.1" TRUE

'''

s = "192.168.1.1"
parts = s.split(".")
valid = True
if len(parts) != 4:
    valid = False
else:
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            valid = False
print("Valid IP:", valid)