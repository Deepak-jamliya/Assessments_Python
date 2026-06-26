def cvowels(s):
    name = s.split()
    vowels = 'aeiouAEIOU'
    count = 0
    for i in name:
        if i[0] in vowels:
            count+=1
    return count