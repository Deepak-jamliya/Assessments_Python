logins = ["Deepak","Gourav","Deepak","Abhijeet","Kuldeep"]
d = {}

for i in logins:
    l = len(i)
    if l not in d:
        d[l] = []
    d[l].append(i)

print(d)