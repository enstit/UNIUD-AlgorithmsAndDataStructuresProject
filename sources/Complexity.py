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

# Create an array with random strings
# with individual lengths from sizes array
strings = []
for size in sizes:
    strings.append(''.join(
            random.choices(['a','b','c'], k=size)
        ))

############################################################

# Create an array with timings from PeriodNaive function
# with input from strings array
growth_PN = []
for s in strings:
    start = t.time()
    PeriodNaive(s)
    end = t.time()
    growth_PN.append(end-start)

# Create an array with timings from PeriodSmart function
# with input from strings array
growth_PS = []
for s in strings:
    start = t.time()
    PeriodSmart(s)
    end = t.time()
    growth_PS.append(end-start)

############################################################

import csv

row_list = [['size', 'time_PN', 'time_PS']]
for i in range(RANGE):
    row_list.append([sizes[i], growth_PN[i], growth_PS[i]])

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