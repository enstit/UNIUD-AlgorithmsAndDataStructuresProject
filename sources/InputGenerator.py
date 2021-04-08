import random

def InputGenerator(first_size, last_size, span):
    sizes = _getSizes(first_size, last_size, span)
    strings = []
    for size in sizes:
        strings.append(_StringGenerator_3(size))
    return strings

# Create an array with exponential sizes
# in range(FIRST_SIZE,LAST_SIZE)
def _getSizes(first_size, last_size, span):
    sizes = []
    a = first_size
    b = (last_size/first_size)**(float(1/(span-1)))
    for i in range(span):
        sizes.append(int(a*(b**i)))
    return sizes

# Create a random string of size 'size'
def _StringGenerator_1(size):
    return ''.join(random.choices(['a','b','c'], k=size))

# Create a string of size 'size' generated as follows:
# generated a random position for the array,
# then fill the string randomly until this position,
# then copy chars from the start of the string
# until string size is completed
def _StringGenerator_2(size):
    q = random.randint(1, size)
    s = (''.join(random.choices(['a', 'b', 'c'], k=q)))
    for i in range(q+1, size+1):
        s = s + s[((i-1)%q +1)]
    return s

# Create a string of size 'size' using the same
# method of '_InputGenerator_2', but the character in position
# q will be different from the others ('d')
def _StringGenerator_3(size):
    q = random.randint(1, size)
    s = (''.join(random.choices(['a', 'b', 'c'], k=q-1)))
    s = s + 'd'
    for i in range(q+1, size+1):
        s = s + s[((i-1)%q)]
    return s

# Create a string of size 'size' in the form
# 'abcaabbccaaabbbccc...'
# This is also the worst input pattern for
# PeriodNaive algorithm
def _StringGenerator_4(size):
    i = 0
    s = ''
    while len(s)<=size:
        s = s + 'a'*i + 'b'*i + 'c'*i
        i += 1
    return s[:size+1]