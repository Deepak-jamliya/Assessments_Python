def factors(n):
    ans = []
    for i in range(1,n//2+1):
        if n%i == 0:
            ans.append(i)
    return ans