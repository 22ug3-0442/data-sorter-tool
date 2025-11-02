import time

def merge(left, right):
    i = j = 0
    merged = []
    steps = 0

    while i < len(left) and j < len(right):
        steps += 1  # comparison
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        steps += 1  # writing to merged

    # Copy remaining elements
    while i < len(left):
        merged.append(left[i])
        i += 1
        steps += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
        steps += 1

    return merged, steps


def merge_sort(a):
    if len(a) <= 1:
        return a.copy(), 0

    mid = len(a) // 2
    left, l_steps = merge_sort(a[:mid])
    right, r_steps = merge_sort(a[mid:])
    merged, m_steps = merge(left, right)

    return merged, l_steps + r_steps + m_steps

