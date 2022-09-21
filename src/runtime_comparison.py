################################################################
# libraries:
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

################################################################
# functions:
from lin import ba_algorithm
from naive import naive_algorithm
from SEQsimulator import simulate_string
from SEQsimulator import get_exact_read

################################################################
# tests:
    
    
# Test against re.finditer():
for i in range(500000):
    #print('Iteration nr: ', i+1)
    ref = simulate_string(random.randint(50,100))
    read = get_exact_read(ref, random.randint(1,20))
    re_findings = [m.start() for m in re.finditer('(?={0})'.format(re.escape(read)), ref)]
    if naive_algorithm(ref,read) != re_findings:
        print('Algorithm mistake!')
        break
    if i == 499999:
        print('DONE')


# Test lin vs naive for same result:
for i in range(500000):
    #print('Iteration nr: ', i+1)
    ref = simulate_string(random.randint(30,90))
    read = get_exact_read(ref, random.randint(1,20))
    if naive_algorithm(ref,read) != ba_algorithm(ref,read):
        print('Algorithm mistake!')
        break
    if i == 499999:
        print('DONE')


# runtimes for the naive algorithm:
ref_lengths = [25000,50000,75000,100000,125000]
read_lengths_100 = [100]*5
read_lengths_200 = [200]*5
read_lengths_300 = [300]*5
read_lengths_400 = [400]*5
read_lengths_500 = [500]*5
runtimes_naive_100 = []
runtimes_naive_200 = []
runtimes_naive_300 = []
runtimes_naive_400 = []
runtimes_naive_500 = []
for idx in range(5):
    print('Iteration nr: ', idx+1)
    runtimes_naive_100_replicate = []
    runtimes_naive_200_replicate = []
    runtimes_naive_300_replicate = []
    runtimes_naive_400_replicate = []
    runtimes_naive_500_replicate = []
    for i in range(10):
        
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths_100[idx])
        start_time = time.time()
        naive_algorithm(ref,read)
        end_time = time.time()
        runtimes_naive_100_replicate.append(end_time-start_time)
        
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths_200[idx])
        start_time = time.time()
        naive_algorithm(ref,read)
        end_time = time.time()
        runtimes_naive_200_replicate.append(end_time-start_time)
        
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths_300[idx])
        start_time = time.time()
        naive_algorithm(ref,read)
        end_time = time.time()
        runtimes_naive_300_replicate.append(end_time-start_time)
        
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths_400[idx])
        start_time = time.time()
        naive_algorithm(ref,read)
        end_time = time.time()
        runtimes_naive_400_replicate.append(end_time-start_time)
        
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths_500[idx])
        start_time = time.time()
        naive_algorithm(ref,read)
        end_time = time.time()
        runtimes_naive_500_replicate.append(end_time-start_time)
        
    runtimes_naive_100.append(np.mean(runtimes_naive_100_replicate))
    runtimes_naive_200.append(np.mean(runtimes_naive_200_replicate))
    runtimes_naive_300.append(np.mean(runtimes_naive_300_replicate))
    runtimes_naive_400.append(np.mean(runtimes_naive_400_replicate))
    runtimes_naive_500.append(np.mean(runtimes_naive_500_replicate))
# plot running times:
fig, ax = plt.subplots()
sns.lineplot(x=ref_lengths, y=runtimes_naive_100, ax=ax, label='read length = 100')
sns.lineplot(x=ref_lengths, y=runtimes_naive_200, ax=ax, label='read length = 200')
sns.lineplot(x=ref_lengths, y=runtimes_naive_300, ax=ax, label='read length = 300')
sns.lineplot(x=ref_lengths, y=runtimes_naive_400, ax=ax, label='read length = 400')
sns.lineplot(x=ref_lengths, y=runtimes_naive_500, ax=ax, label='read length = 500')
plt.xlabel('ref length')
plt.ylabel('runtime (s)')
plt.ylim(0, 0.17)
plt.tight_layout()
plt.show()

# runtimes for the naive algorithm (BEST CASE):
ref_lengths = [25000,50000,75000,100000,125000]
read_lengths_500 = [500]*5
runtimes_naive_500 = []
runtimes_naive_BEST_case = []
for idx in range(5):
    print('Iteration nr: ', idx+1)
    runtimes_naive_500_replicate = []
    runtimes_BEST_case_replicates = []
    for i in range(2):
        
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths_500[idx])
        start_time = time.time()
        naive_algorithm(ref,read)
        end_time = time.time()
        runtimes_naive_500_replicate.append(end_time-start_time)
        
        ref = 'A'*ref_lengths[idx]
        read = 'T'*500
        start_time = time.time()
        naive_algorithm(ref,read)
        end_time = time.time()
        runtimes_BEST_case_replicates.append(end_time-start_time)
        
    runtimes_naive_500.append(np.mean(runtimes_naive_500_replicate))
    runtimes_naive_BEST_case.append(np.mean(runtimes_BEST_case_replicates))
# plot running times:
fig, ax = plt.subplots()
sns.lineplot(x=ref_lengths, y=runtimes_naive_500, ax=ax, label='read length = 500', color='purple')
sns.lineplot(x=ref_lengths, y=runtimes_naive_BEST_case, ax=ax, label='teoretical_BEST_case', color='black')
plt.xlabel('ref length')
plt.ylabel('runtime (s)')
plt.tight_layout()
plt.show()

# runtimes for the naive algorithm (WORST CASE):
ref_lengths = [25000,50000,75000,100000,125000]
read_lengths_500 = [500]*5
runtimes_naive_500 = []
runtimes_naive_WORST_case = []
for idx in range(5):
    print('Iteration nr: ', idx+1)
    runtimes_naive_500_replicate = []
    runtimes_WORST_case_replicates = []
    for i in range(2):
        
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths_500[idx])
        start_time = time.time()
        naive_algorithm(ref,read)
        end_time = time.time()
        runtimes_naive_500_replicate.append(end_time-start_time)
        
        ref = 'A'*ref_lengths[idx]
        read = 'A'*500
        start_time = time.time()
        naive_algorithm(ref,read)
        end_time = time.time()
        runtimes_WORST_case_replicates.append(end_time-start_time)
        
    runtimes_naive_500.append(np.mean(runtimes_naive_500_replicate))
    runtimes_naive_WORST_case.append(np.mean(runtimes_WORST_case_replicates))
# plot running times:
fig, ax = plt.subplots()
sns.lineplot(x=ref_lengths, y=runtimes_naive_500, ax=ax, label='read length = 500', color='purple')
sns.lineplot(x=ref_lengths, y=runtimes_naive_WORST_case, ax=ax, label='teoretical_worst_case', color='black')
plt.xlabel('ref length')
plt.ylabel('runtime (s)')
plt.tight_layout()
plt.show()


# runtimes for the linear algorithm:
ref_lengths = [25000,50000,75000,100000,125000]
read_lengths_100 = [100]*5
read_lengths_200 = [200]*5
read_lengths_300 = [300]*5
read_lengths_400 = [400]*5
read_lengths_500 = [500]*5
runtimes_lin_100 = []
runtimes_lin_200 = []
runtimes_lin_300 = []
runtimes_lin_400 = []
runtimes_lin_500 = []
for idx in range(5):
    print('Iteration nr: ', idx+1)
    runtimes_lin_100_replicate = []
    runtimes_lin_200_replicate = []
    runtimes_lin_300_replicate = []
    runtimes_lin_400_replicate = []
    runtimes_lin_500_replicate = []
    for i in range(10):
        
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths_100[idx])
        start_time = time.time()
        ba_algorithm(ref,read)
        end_time = time.time()
        runtimes_lin_100_replicate.append(end_time-start_time)
        
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths_200[idx])
        start_time = time.time()
        ba_algorithm(ref,read)
        end_time = time.time()
        runtimes_lin_200_replicate.append(end_time-start_time)
        
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths_300[idx])
        start_time = time.time()
        ba_algorithm(ref,read)
        end_time = time.time()
        runtimes_lin_300_replicate.append(end_time-start_time)
        
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths_400[idx])
        start_time = time.time()
        ba_algorithm(ref,read)
        end_time = time.time()
        runtimes_lin_400_replicate.append(end_time-start_time)
        
        ref = simulate_string(ref_lengths[idx])
        read = get_exact_read(ref, read_lengths_500[idx])
        start_time = time.time()
        ba_algorithm(ref,read)
        end_time = time.time()
        runtimes_lin_500_replicate.append(end_time-start_time)
        
    runtimes_lin_100.append(np.mean(runtimes_lin_100_replicate))
    runtimes_lin_200.append(np.mean(runtimes_lin_200_replicate))
    runtimes_lin_300.append(np.mean(runtimes_lin_300_replicate))
    runtimes_lin_400.append(np.mean(runtimes_lin_400_replicate))
    runtimes_lin_500.append(np.mean(runtimes_lin_500_replicate))
# plot running times:
fig, ax = plt.subplots()
sns.lineplot(x=ref_lengths, y=runtimes_lin_100, ax=ax, label='read length = 100')
sns.lineplot(x=ref_lengths, y=runtimes_lin_200, ax=ax, label='read length = 200')
sns.lineplot(x=ref_lengths, y=runtimes_lin_300, ax=ax, label='read length = 300')
sns.lineplot(x=ref_lengths, y=runtimes_lin_400, ax=ax, label='read length = 400')
sns.lineplot(x=ref_lengths, y=runtimes_lin_500, ax=ax, label='read length = 500')
plt.xlabel('ref length')
plt.ylabel('runtime (s)')
plt.ylim(0, 0.17)
plt.tight_layout()
plt.show()

