from PeriodNaive import PeriodNaive
from PeriodSmart import PeriodSmart
import matplotlib.pyplot as plt
import random

############################################################

# System time resolution
import time as t

TIME_ERROR = 0.001

start = t.time()
end = t.time()

while (start == end):
    end = t.time()

r = end - start
t_min = r*((1/TIME_ERROR)+1)

############################################################

# Set choosen parameters
FIRST_SIZE = 1_000
LAST_SIZE = 500_000
RANGE = 100

# Create an array with exponential sizes
# in range(FIRST_SIZE,LAST_SIZE)
sizes = []
a = FIRST_SIZE
b = (LAST_SIZE/FIRST_SIZE)**(float(1/(RANGE-1)))
for i in range(RANGE):
    sizes.append(int(a*(b**i)))

############################################################

# Set choosen method for generating inputs
METHOD = 'Random2' # 'Random1' | 'Random2'

if (METHOD == 'Random1'):
    # Create an array with random strings
    # with individual lengths from sizes array
    strings = []
    for size in sizes:
        strings.append(''.join(
                random.choices(['a','b','c'], k=size)
                ))
elif(METHOD == 'Random2'):
    # Create an array with strings generated as follows:
    # generated a random position for the array,
    # then fill the string randomly until this position,
    # then copy chars from the start of the string
    # until string size is completed
    strings = []
    for size in sizes:
        q = random.randint(1, size)
        s = (''.join(random.choices(['a', 'b', 'c'], k=q)))
        for i in range(q+1, size+1):
            s = s + s[(i-1) % q + 1]
        strings.append(s)

############################################################

# Create an array with average timings from PeriodNaive
growth_PN = []
for s in strings:
    i = 0
    t_passed = 0
    while ( t_passed <= t_min ):
        start = t.time()
        PeriodNaive(s)
        end = t.time()
        i += 1
        t_passed += end-start
    growth_PN.append(t_passed/i)

# Create an array with average timings from PeriodSmart
growth_PS = []
for s in strings:
    i = 0
    t_passed = 0
    while ( t_passed <= t_min ):
        start = t.time()
        PeriodSmart(s)
        end = t.time()
        i += 1
        t_passed += end-start
    growth_PS.append(t_passed/i)

############################################################

import csv

row_list = [['id', 'size', 'time_PN', 'time_PS']]
for i in range(RANGE):
    row_list.append([i, sizes[i], growth_PN[i], growth_PS[i]])

with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

############################################################

plt.figure(figsize=(10, 6))
plt.plot(sizes, growth_PN, linestyle='-', marker='.', label = "PeriodNaive")
plt.plot(sizes, growth_PS, linestyle='-', marker='.', label = "PeriodSmart")
plt.title('Average timings for random inputs')
plt.xlabel('Input size')
plt.xscale('linear') # 'linear'|'log'
plt.xlim(FIRST_SIZE,LAST_SIZE) 
plt.ylabel('Timing') 
plt.yscale('linear') # 'linear'|'log'
plt.legend() 
plt.show()