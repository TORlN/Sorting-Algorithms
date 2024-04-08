import random
import math
from copy import deepcopy
import time
import matplotlib.pyplot as plt
import numpy as np
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort1 import shell_sort1
from shell_sort2 import shell_sort2
from shell_sort3 import shell_sort3
from shell_sort4 import shell_sort4
from hybrid_sort1 import hybrid_sort1
from hybrid_sort2 import hybrid_sort2
from hybrid_sort3 import hybrid_sort3


def plot_and_save_best_fit_lines(testN, timings, algorithm_name):
    plt.figure(figsize=(10, 7))
    x_log = np.log(testN)
    colors = ["b", "g", "r"]  # Colors for shuffled, almost sorted, and reversed
    labels = ["Shuffled", "Almost Sorted", "Reversed"]

    # Define a location to start placing text
    y_position = 0.8  # Starting y position for the text, in axes coordinates

    for i, label in enumerate(labels):  # For each input distribution
        y_log = np.log(timings[:, i])
        slope, intercept = np.polyfit(x_log, y_log, 1)
        best_fit_y = np.exp(intercept) * testN**slope

        plt.plot(
            testN, best_fit_y, color=colors[i], label=f"{algorithm_name} - {label}"
        )

        # Create equation string
        equation_str = f"{label}: y = {np.exp(intercept):.2e}x^({slope:.2f})"

        # Place text on the plot
        plt.text(
            0.05,
            y_position,
            equation_str,
            transform=plt.gca().transAxes,
            color=colors[i],
        )
        y_position -= 0.1  # Adjust y position for the next line of text

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Array Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title(f"Best Fit Lines for {algorithm_name} on Log-Log Scale")
    plt.legend()
    plt.grid(True)

    # Save each plot with a unique name based on the algorithm
    plt.savefig(f"{algorithm_name}_Performance.png")
    plt.close()  # Close the plot to free up memory and avoid displaying it inline if not desired


def generateUniformPermutations(n):
    if n == 0:
        return []
    else:
        arr = list(range(1, n + 1))
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr


def randomSwap(arr):
    newNums = deepcopy(arr)
    k = math.floor(2 * math.log2(len(newNums)))
    for _ in range(k):
        j = random.randint(0, len(newNums) - 1)
        i = random.randint(0, len(newNums) - 1)
        newNums[i], newNums[j] = newNums[j], newNums[i]
    return newNums


def testInsertion(sortedNums, shuffledNums, almostSortedNums, reversedNums):
    test1_start = time.time()
    insertion_sort(shuffledNums)
    test1_end = time.time()
    test2_start = time.time()
    insertion_sort(almostSortedNums)
    test2_end = time.time()
    test3_start = time.time()
    insertion_sort(reversedNums)
    test3_end = time.time()
    test1_time = test1_end - test1_start
    test2_time = test2_end - test2_start
    test3_time = test3_end - test3_start
    return test1_time, test2_time, test3_time


def testMerge(sortedNums, shuffledNums, almostSortedNums, reversedNums):
    test1_start = time.time()
    merge_sort(shuffledNums)
    test1_end = time.time()
    test2_start = time.time()
    merge_sort(almostSortedNums)
    test2_end = time.time()
    test3_start = time.time()
    merge_sort(reversedNums)
    test3_end = time.time()
    test1_time = test1_end - test1_start
    test2_time = test2_end - test2_start
    test3_time = test3_end - test3_start
    return test1_time, test2_time, test3_time


def testShell1(sortedNums, shuffledNums, almostSortedNums, reversedNums):
    test1_start = time.time()
    shell_sort1(shuffledNums)
    test1_end = time.time()
    test2_start = time.time()
    shell_sort1(almostSortedNums)
    test2_end = time.time()
    test3_start = time.time()
    shell_sort1(reversedNums)
    test3_end = time.time()
    test1_time = test1_end - test1_start
    test2_time = test2_end - test2_start
    test3_time = test3_end - test3_start
    return test1_time, test2_time, test3_time


def testShell2(sortedNums, shuffledNums, almostSortedNums, reversedNums):
    test1_start = time.time()
    shell_sort2(shuffledNums)
    test1_end = time.time()
    test2_start = time.time()
    shell_sort2(almostSortedNums)
    test2_end = time.time()
    test3_start = time.time()
    shell_sort2(reversedNums)
    test3_end = time.time()
    test1_time = test1_end - test1_start
    test2_time = test2_end - test2_start
    test3_time = test3_end - test3_start
    return test1_time, test2_time, test3_time


def testShell3(sortedNums, shuffledNums, almostSortedNums, reversedNums):
    test1_start = time.time()
    shell_sort3(shuffledNums)
    test1_end = time.time()
    test2_start = time.time()
    shell_sort3(almostSortedNums)
    test2_end = time.time()
    test3_start = time.time()
    shell_sort3(reversedNums)
    test3_end = time.time()
    test1_time = test1_end - test1_start
    test2_time = test2_end - test2_start
    test3_time = test3_end - test3_start
    return test1_time, test2_time, test3_time


def testShell4(sortedNums, shuffledNums, almostSortedNums, reversedNums):
    test1_start = time.time()
    shell_sort4(shuffledNums)
    test1_end = time.time()
    test2_start = time.time()
    shell_sort4(almostSortedNums)
    test2_end = time.time()
    test3_start = time.time()
    shell_sort4(reversedNums)
    test3_end = time.time()
    test1_time = test1_end - test1_start
    test2_time = test2_end - test2_start
    test3_time = test3_end - test3_start
    return test1_time, test2_time, test3_time


def testHybrid1(sortedNums, shuffledNums, almostSortedNums, reversedNums):
    test1_start = time.time()
    hybrid_sort1(shuffledNums)
    test1_end = time.time()
    test2_start = time.time()
    hybrid_sort1(almostSortedNums)
    test2_end = time.time()
    test3_start = time.time()
    hybrid_sort1(reversedNums)
    test3_end = time.time()
    test1_time = test1_end - test1_start
    test2_time = test2_end - test2_start
    test3_time = test3_end - test3_start
    return test1_time, test2_time, test3_time


def testHybrid2(sortedNums, shuffledNums, almostSortedNums, reversedNums):
    test1_start = time.time()
    hybrid_sort2(shuffledNums)
    test1_end = time.time()
    test2_start = time.time()
    hybrid_sort2(almostSortedNums)
    test2_end = time.time()
    test3_start = time.time()
    hybrid_sort2(reversedNums)
    test3_end = time.time()
    test1_time = test1_end - test1_start
    test2_time = test2_end - test2_start
    test3_time = test3_end - test3_start
    return test1_time, test2_time, test3_time


def testHybrid3(sortedNums, shuffledNums, almostSortedNums, reversedNums):
    test1_start = time.time()
    hybrid_sort3(shuffledNums)
    test1_end = time.time()
    test2_start = time.time()
    hybrid_sort3(almostSortedNums)
    test2_end = time.time()
    test3_start = time.time()
    hybrid_sort3(reversedNums)
    test3_end = time.time()
    test1_time = test1_end - test1_start
    test2_time = test2_end - test2_start
    test3_time = test3_end - test3_start
    return test1_time, test2_time, test3_time


def main():
    testN = [100, 500, 1000, 2500, 5000, 10000, 25000]
    insertion_timings = np.zeros((len(testN), 3))
    merge_timings = np.zeros((len(testN), 3))
    shell1_timings = np.zeros((len(testN), 3))
    shell2_timings = np.zeros((len(testN), 3))
    shell3_timings = np.zeros((len(testN), 3))
    shell4_timings = np.zeros((len(testN), 3))
    hybrid1_timings = np.zeros((len(testN), 3))
    hybrid2_timings = np.zeros((len(testN), 3))
    hybrid3_timings = np.zeros((len(testN), 3))
    for i, n in enumerate(testN):
        sortedNums = list(range(1, n + 1))
        shuffledNums = generateUniformPermutations(n)
        almostSortedNums = randomSwap(sortedNums)
        reversedNums = deepcopy(sortedNums)
        reversedNums.reverse()
        # test insertion sort
        insertion_t1, insertion_t2, insertion_t3 = testInsertion(
            sortedNums, shuffledNums, almostSortedNums, reversedNums
        )
        insertion_timings[i] = [insertion_t1, insertion_t2, insertion_t3]
        # test merge sort
        merge_t1, merge_t2, merge_t3 = testMerge(
            sortedNums, shuffledNums, almostSortedNums, reversedNums
        )
        merge_timings[i] = [merge_t1, merge_t2, merge_t3]
        # test shell sort 1
        shell1_t1, shell1_t2, shell1_t3 = testShell1(
            sortedNums, shuffledNums, almostSortedNums, reversedNums
        )
        shell1_timings[i] = [shell1_t1, shell1_t2, shell1_t3]
        # test shell sort 2
        shell2_t1, shell2_t2, shell2_t3 = testShell2(
            sortedNums, shuffledNums, almostSortedNums, reversedNums
        )
        shell2_timings[i] = [shell2_t1, shell2_t2, shell2_t3]
        # test shell sort 3
        shell3_t1, shell3_t2, shell3_t3 = testShell3(
            sortedNums, shuffledNums, almostSortedNums, reversedNums
        )
        shell3_timings[i] = [shell3_t1, shell3_t2, shell3_t3]
        # test shell sort 4
        shell4_t1, shell4_t2, shell4_t3 = testShell4(
            sortedNums, shuffledNums, almostSortedNums, reversedNums
        )
        shell4_timings[i] = [shell4_t1, shell4_t2, shell4_t3]
        # test hybrid sort 1
        hybrid1_t1, hybrid1_t2, hybrid1_t3 = testHybrid1(
            sortedNums, shuffledNums, almostSortedNums, reversedNums
        )
        hybrid1_timings[i] = [hybrid1_t1, hybrid1_t2, hybrid1_t3]
        # test hybrid sort 2
        hybrid2_t1, hybrid2_t2, hybrid2_t3 = testHybrid2(
            sortedNums, shuffledNums, almostSortedNums, reversedNums
        )
        hybrid2_timings[i] = [hybrid2_t1, hybrid2_t2, hybrid2_t3]
        # test hybrid sort 3
        hybrid3_t1, hybrid3_t2, hybrid3_t3 = testHybrid3(
            sortedNums, shuffledNums, almostSortedNums, reversedNums
        )
        hybrid3_timings[i] = [hybrid3_t1, hybrid3_t2, hybrid3_t3]

    plot_and_save_best_fit_lines(testN, insertion_timings, "Insertion Sort")
    plot_and_save_best_fit_lines(testN, merge_timings, "Merge Sort")
    plot_and_save_best_fit_lines(testN, shell1_timings, "Shell Sort 1")
    plot_and_save_best_fit_lines(testN, shell2_timings, "Shell Sort 2")
    plot_and_save_best_fit_lines(testN, shell3_timings, "Shell Sort 3")
    plot_and_save_best_fit_lines(testN, shell4_timings, "Shell Sort 4")
    plot_and_save_best_fit_lines(testN, hybrid1_timings, "Hybrid Sort 1")
    plot_and_save_best_fit_lines(testN, hybrid2_timings, "Hybrid Sort 2")
    plot_and_save_best_fit_lines(testN, hybrid3_timings, "Hybrid Sort 3")


if __name__ == "__main__":
    main()
