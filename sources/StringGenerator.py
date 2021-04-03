import random


def inputGenerator1(size):
    return ''.join(random.choices(['a', 'b', 'c'], k=size))


def inputGenerator2(size):
    q = random.randint(1, size)
    s = (''.join(random.choices(['a', 'b', 'c'], k=q)))
    for i in range(q + 1, size + 1):
        s = s + s[i % q]
    return s


def inputGenerator3(size):
    q = random.randint(1, size)
    s = (''.join(random.choices(['a', 'b', 'c'], k=q - 1)))
    s = s + 'd'
    for i in range(q + 1, size + 1):
        s = s + s[i % q]  # s = s + s[(i-1) % q + 1]
    return s
