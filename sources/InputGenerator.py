import random

def InputGenerator(first_size, last_size, span):
    sizes = _getSizes(first_size, last_size, span)
    strings = []
    for size in sizes:
        strings.append(_InputGenerator_3(size))
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

# Create an array with random strings
# with individual lengths from sizes array
def _InputGenerator_1(size):
    return ''.join(random.choices(['a','b','c'], k=size))

# Create an array with strings generated as follows:
# generated a random position for the array,
# then fill the string randomly until this position,
# then copy chars from the start of the string
# until string size is completed
def _InputGenerator_2(size):
    q = random.randint(1, size)
    s = (''.join(random.choices(['a', 'b', 'c'], k=q)))
    for i in range(q+1, size+1):
        s = s + s[((i-1) % q)]
    return s

# Create an array with strings using the same
# method of 'Random2', but the character in position
# q will be different from the others ('d')
def _InputGenerator_3(size):
    q = random.randint(1, size)
    s = (''.join(random.choices(['a', 'b', 'c'], k=q-1)))
    s = s + 'd'
    for i in range(q+1, size+1):
        s = s + s[((i-1) % q+1)]
    return s
