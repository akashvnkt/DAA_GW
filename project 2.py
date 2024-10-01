import time
import random

# Helper function for insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Median of Medians algorithm implementation
def median_of_medians(arr, k):
    if len(arr) <= 5:
        sorted_arr = insertion_sort(arr)
        return sorted_arr[k]

    # Divide array into groups of 5
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Find the median of each group
    medians = [insertion_sort(sublist)[len(sublist) // 2] for sublist in sublists]

    # Find the median of medians
    median_of_medians_value = median_of_medians(medians, len(medians) // 2)

    # Partition the array around the median of medians
    low = [x for x in arr if x < median_of_medians_value]
    high = [x for x in arr if x > median_of_medians_value]
    equal = [x for x in arr if x == median_of_medians_value]

    # Recurse based on the value of k
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(equal):
        return median_of_medians_value
    else:
        return median_of_medians(high, k - len(low) - len(equal))


# QuickSelect function
def quickselect(arr, k):
    return median_of_medians(arr, k)

values_of_n=[]

# Function to measure the execution time for different values of n
def measure_time():
    results = []
    values_of_n = [10 ** i for i in range(1, 12)]  # Values of n: 10, 100, ..., 10^11

    for idx, n in enumerate(values_of_n, start=1):
        # Generate a random array of size n
        array = random.sample(range(1, n + 1), min(n, 10 ** 6))  # limiting array size to avoid memory issues
        k = len(array) // 2  # Find the median

        # Measure the execution time in nanoseconds
        start_time = time.time_ns()
        quickselect(array, k)
        end_time = time.time_ns()

        # Calculate elapsed time in nanoseconds
        elapsed_time_ns = end_time - start_time

        # Store the results
        results.append([idx, n, elapsed_time_ns])
        print(f"n = {n}, Time taken: {elapsed_time_ns} nanoseconds")

    return results

# Get the timing results
results = measure_time()

# Save results to an Excel-compatible CSV file
import csv

with open('quickselect_median_of_medians_analysis.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(["S no", "Values of n", "Experimental values (s)"])
    # Writing the data
    for row in results:
        writer.writerow(row)

