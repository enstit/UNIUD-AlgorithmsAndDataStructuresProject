# Returns the minimum fractional period of s
def PeriodNaive(s):
    n = len(s)
    for p in range(1,n+1):
        if(_isPeriod(s,p)):
            return p
    return 0 # The input is an empty string

# Returns True if p is a fractional period of s,
# False otherwhise.
def _isPeriod(s,p):
    n = len(s)
    return (s[:n-p] == s[p:])
     
##############################

# Returns True if p is a fractional period of s,
# False otherwhise.
def _isPeriod_2(s,p):
    n = len(s)
    for j in range(0,n-p):
        if(s[j] != s[j+p]):
            return False
    return True