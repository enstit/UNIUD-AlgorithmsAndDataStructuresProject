# Returns the minimum fractional period of s
def PeriodSmart(s):
    if(s == ""):
        return -1
    n = len(s)
    pf = [None] * n
    pf[0] = 0
    for i in range (1, n):
        j = pf[i-1]
        while j > 0 and s[i] != s[j]:
            j = pf[j-1]
        if s[i] == s[j]:
            j += 1
        pf[i] = j
    maxValue = pf[n-1]
    return n - maxValue

# Returns True if string t is a Border of string s
def isStringBorder(t, s):
    n_t = len(t)
    n_s = len(s)
    return ((s[:n_t] == t) and (s[n_s-n_t:] == t))
