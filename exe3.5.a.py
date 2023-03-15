import time
import random
import numpy as np
import matplotlib.pyplot as plt

#Inefficient implementation
def inefficient(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#Efficient implementation
def efficient(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def experiment():
    sizes = [1000, 10000, 100000]
    measurements = 100

    inefficient_times = []
    efficient_times = []

    for size in sizes:
        arr = sorted(random.sample(range(size), size))
        target = random.randint(0, size - 1)
        inefficient_total_time = 0
        efficient_total_time = 0
        for i in range(measurements):
            start_time = time.time()
            inefficient(arr, target)
            end_time = time.time()
            inefficient_total_time += end_time - start_time

            start_time = time.time()
            efficient(arr, target)
            end_time = time.time()
            efficient_total_time += end_time - start_time

        inefficient_avg_time = inefficient_total_time / measurements
        efficient_avg_time = efficient_total_time / measurements

        inefficient_times.append(inefficient_avg_time)
        efficient_times.append(efficient_avg_time)

        print(f"Size: {size}")
        print(f"Inefficient average time: {inefficient_avg_time}")
        print(f"Efficient search average time: {efficient_avg_time}")

    plt.plot(sizes, inefficient_times, label="Inefficient")
    plt.plot(sizes, efficient_times, label="Efficient search")
    plt.xlabel("Array size")
    plt.ylabel("Average time (seconds)")
    plt.legend()
    plt.show()

experiment()
