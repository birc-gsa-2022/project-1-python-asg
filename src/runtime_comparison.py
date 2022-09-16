################################################################
# libraries:
import time
import random
import numpy as np
import matplotlib.pyplot as plt

################################################################
# functions:
from lin import ba_algorithm
from naive import naive_algorithm
from SEQsimulator import simulate_string
from SEQsimulator import get_exact_read

################################################################
# tests:
    
# Test lin vs naive for same result:
# for i in range(10000):
#     ref = simulate_string(random.randint(100,1000))
#     read = get_exact_read(ref, random.randint(1,100))
#     if naive_algorithm(ref,read) != ba_algorithm(ref,read):
#         print(False)

# Testing running time:
ref_lengths = [2000,3000,4000,5000,6000,7000,8000]
read_lengths = [4**2,8**2,16**2,20**2,24**2,28**2,32**2]
runtimes_naive = []
runtimes_lin = []
for idx in range(7):
    naive_replicate = []
    lin_replicate = []
    for i in range(100):
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths[idx])
        start_time = time.time()
        naive_algorithm(ref,read)
        end_time = time.time()
        naive_replicate.append(end_time-start_time)
        start_time = time.time()
        ba_algorithm(ref, read)
        end_time = time.time()
        lin_replicate.append(end_time-start_time)
    runtimes_lin.append(np.mean(lin_replicate))
    runtimes_naive.append(np.mean(naive_replicate))
    
fig, ax = plt.subplots()
ax.plot(ref_lengths,runtimes_naive, color='firebrick', linewidth=3)
ax.scatter(x=ref_lengths, y=runtimes_naive, color='black', marker='.', alpha=1)
ax.plot(ref_lengths,runtimes_lin, color='cornflowerblue', linewidth=3)
ax.scatter(x=ref_lengths, y=runtimes_lin, color='black', marker='.', alpha=1)
plt.grid(True) 
plt.show()
plt.close()
