from PeriodNaive import PeriodNaive
from PeriodSmart import PeriodSmart
from InputGenerator import InputGenerator
import matplotlib.pyplot as plt

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

# Set chosen parameters
FIRST_SIZE = 1_000
LAST_SIZE = 500_000
RANGE = 100

# Generate input array
strings = InputGenerator(FIRST_SIZE,LAST_SIZE,RANGE)

############################################################

# Create an array with average timings from PeriodNaive
growth_PN = []
results_PN = []
for s in strings:
    i = 0
    t_passed = 0
    while ( t_passed <= t_min ):
        start = t.time()
        result = PeriodNaive(s)
        end = t.time()
        i += 1
        t_passed += end-start
    results_PN.append(result)
    growth_PN.append(t_passed/i)

# Create an array with average timings from PeriodSmart
growth_PS = []
results_PS = []
for s in strings:
    i = 0
    t_passed = 0
    while ( t_passed <= t_min ):
        start = t.time()
        result = PeriodSmart(s)
        end = t.time()
        i += 1
        t_passed += end-start
    results_PS.append(result)
    growth_PS.append(t_passed/i)

############################################################

import csv

row_list = [['id', 'size', 'result_PN', 'time_PN', 'result_PS', 'time_PS']]
for i in range(RANGE):
    row_list.append([i, len(strings[i]), results_PN[i], growth_PN[i], results_PS[i], growth_PS[i]])

with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

############################################################

# plt.figure(figsize=(10, 6))
# plt.plot(sizes, growth_PN, linestyle='-', marker='.', label = "PeriodNaive")
# plt.plot(sizes, growth_PS, linestyle='-', marker='.', label = "PeriodSmart")
# plt.title('Average timings for random inputs')
# plt.xlabel('Input size')
# plt.xscale('linear') # 'linear'|'log'
# plt.xlim(FIRST_SIZE,LAST_SIZE) 
# plt.ylabel('Timing') 
# plt.yscale('linear') # 'linear'|'log'
# plt.legend() 
# plt.show()
