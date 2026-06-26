def dup(n):
    f = []
    for i in n:
        if i not in f:
            f.append(i)
    return f