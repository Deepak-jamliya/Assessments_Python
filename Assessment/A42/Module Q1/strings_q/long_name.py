def longest(s):
    names = s.split()
    highest = names[0]
    for i in names:
        if len(i) > len(highest):
            highest = i
    return highest