# FIXED SIZE MONTE-CARLO

# THE AVERAGES ARE COMPUTED AT EACH TIME STEP.
############################################

# save magnetizations in a list for each seed
file2 = open("data_2.dat", "r")
lines = file2.readlines() 
SEEDS = [[] for i in range(10)]
MAGNETIZATION = []
seed = 0
for line in lines:
       if len(line.strip()) != 0:
              t,M = line.split() 
              MAGNETIZATION.append(abs(float(M)))
       if len(line.strip()) == 0 and len(MAGNETIZATION) > 0:
              SEEDS[seed] = MAGNETIZATION
              MAGNETIZATION = []
              seed += 1
file2.close()

# compute averages at each time step
file4 = open("data_4.dat", "w")
for t in range(len(SEEDS[0])):
       sum = 0
       for seed in range(10):
              sum += SEEDS[seed][t]
       file4.write(f"{t} {sum/10} \n")
file4.close()
############################################

# CONTINUOUS TIME MONTE-CARLO

# THE AVERAGES ARE COMPUTED OVER A WINDOW OF TIME DEFINDED BY THE time_step VARIABLE
# THIS AVERAGE HAS TO BE CALCULATED LIKE THIS BECAUSE AT HIGHT TIMES THERE ARE LESS POINTS
# AND IF WE COMPUTE IT AT EACH TIME STEP THE AVERAGE IS NOT CORRECT.
############################################

# save times and magnetizations in two lists for each seed
file3 = open("data_3.dat", "r")
lines = file3.readlines() 
SEEDS = [[] for i in range(10)]
TIMES = [[] for i in range(10)]
STEP = []
MAGNETIZATION = []
seed = 0
time = 0
for line in lines:
       if len(line.strip()) != 0:
              t,M = line.split() 
              STEP.append(int(t))
              MAGNETIZATION.append(abs(float(M)))
       if len(line.strip()) == 0 and len(MAGNETIZATION) > 0:
              SEEDS[seed] = MAGNETIZATION
              TIMES[time] = STEP
              MAGNETIZATION = []
              STEP = []
              seed += 1
              time += 1

file3.close()
file5 = open("data_5.dat", "w")

# compute the average over a window of time and save it in a file
time_step = 20
n_time_steps = int(10_000/time_step)
averages_times_list = [[] for i in range(n_time_steps)]
for seed in range(10):
       for index,t in enumerate(TIMES[seed]):
              a = 0
              b = time_step
              for i in range(n_time_steps):
                     if t >= a and t < b:
                            averages_times_list[i].append(SEEDS[seed][index])
                            break
                     a += time_step
                     b += time_step
for i in range(len(averages_times_list)):
       sum = 0
       for j in range(len(averages_times_list[i])):
              sum += averages_times_list[i][j]
       if len(averages_times_list[i]) != 0:
              file5.write(f"{i*time_step+1} {sum/len(averages_times_list[i])} \n")