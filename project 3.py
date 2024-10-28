import time
import numpy as np


def maximum_sum_in_array(arr, k):
    n = len(arr)
    MS = np.zeros((k + 1, n))  # 2D array (k+1) x len(arr)
    b_track = np.zeros((k + 1, n))  # Backtrack array

    # Base case for k = 0
    MS[0][0] = arr[0]
    MS[0][1] = max(arr[1], MS[0][0])

    for i in range(2, n):
        MS[0][i] = max(MS[0][i - 1], MS[0][i - 2] + arr[i])

    # Handling the base cases for k ≥ 1 for first and second indices
    for j in range(1, k + 1):
        MS[j][0] = arr[0]
        MS[j][1] = arr[0] + arr[1]

    # Populating MS array for k ≥ 1
    for j in range(1, k + 1):
        for i in range(2, n):
            MS[j][i] = max(MS[j][i - 1],
                             MS[j - 1][i - 1] + arr[i],
                             MS[j][i - 2] + arr[i])

            # Backtrack population
            if MS[j][i] == MS[j][i - 1]:
                b_track[j][i] = 0  # No new addition
            elif MS[j][i] == MS[j - 1][i - 1] + arr[i]:
                b_track[j][i] = 1  # New addition, include arr[i]
            else:
                b_track[j][i] = 1  # New addition, include arr[i], but skip one

    return MS[k][n - 1], b_track[-1]


# Testing with different values of n and k
n_values = [10, 20, 50, 100, 200, 300, 500, 700, 1000, 1500, 2000, 3000, 4000, 5000, 10000]
execution_times = []

for n in n_values:
    arr = np.random.randint(1, 1000, size=n)  # Random array values
    k = np.random.randint(1, 31)  # Random k between 1 and 30

    start_time = time.perf_counter_ns()
    maximum_sum_in_array(arr, k)
    end_time = time.perf_counter_ns()

    execution_time = end_time - start_time
    execution_times.append((n, k, execution_time))
    print(f'n={n}, k={k}, Execution Time (ns): {execution_time}')
