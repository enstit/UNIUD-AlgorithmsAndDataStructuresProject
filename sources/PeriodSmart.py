# Returns the minimum fractional period of s
def PeriodSmart(s):
    n = len(s)
    pf = [0]
    for i in range (1, n):
        j = pf[i-1]
        while ((j > 0) and (s[i] != s[j])):
            j = pf[j-1]
        if (s[i] == s[j]):
            j += 1
        pf.append(j)
    return n - pf[n-1]
