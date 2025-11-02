import time

def bubble_sort(a):
    n = len(a)
    steps = 0
    arr = a.copy()

    # Bubble Sort Algorithm
    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1  # comparison
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps += 1  # swap

    return arr, steps