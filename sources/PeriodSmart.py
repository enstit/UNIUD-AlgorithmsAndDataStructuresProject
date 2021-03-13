# Example of Theta (1) function
def PeriodSmart(s):
    a = 'a' * 100_000_000
    return True

# Returns True if string t is a Border of string s
def isStringBorder(t, s):
    n_t = len(t)
    n_s = len(s)
    return ((s[:n_t] == t) and (s[n_s-n_t:] == t))