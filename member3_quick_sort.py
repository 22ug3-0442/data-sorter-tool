import time

def partition(arr, low, high):
    steps = 0
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        steps += 1  # comparison
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            steps += 1  # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps += 1  # final pivot swap
    return i + 1, steps


def quick_sort(a):
    arr = a.copy()
    steps = 0

    def _qs(low, high):
        nonlocal steps, arr
        if low < high:
            p, ps = partition(arr, low, high)
            steps += ps
            _qs(low, p - 1)
            _qs(p + 1, high)

    _qs(0, len(arr) - 1)
    return arr, steps
