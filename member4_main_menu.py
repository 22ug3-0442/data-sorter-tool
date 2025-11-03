import random
import time
from member1_bubble_sort import bubble_sort
from member2_merge_sort import merge_sort
from member3_quick_sort import quick_sort

# Utility function to time algorithms
def timed_run(func, arr):
    start = time.perf_counter()
    sorted_list, steps = func(arr.copy())
    elapsed = time.perf_counter() - start
    return {"sorted": sorted_list, "steps": steps, "time": elapsed}


def print_table(results_dict, original_data):
    print(f"\n{'Algorithm':<12} {'Time(s)':<10} {'Steps':<12} {'Correct':<8}")
    for name, res in results_dict.items():
        correct = res["sorted"] == sorted(original_data)
        print(f"{name:<12} {res['time']:<10.6f} {res['steps']:<12} {str(correct):<8}")


def main():
    data = []
    while True:
        print("\n--- Data Sorter: Sorting Algorithm Comparison Tool ---")
        print("1. Enter numbers manually")
        print("2. Generate random numbers")
        print("3. Perform Bubble Sort")
        print("4. Perform Merge Sort")
        print("5. Perform Quick Sort")
        print("6. Compare all algorithms (show performance table)")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            s = input("Enter numbers separated by spaces: ")
            data = [int(x) for x in s.split()]

        elif choice == '2':
            n = int(input("Enter number of elements: "))
            lo = int(input("Min value: "))
            hi = int(input("Max value: "))
            data = [random.randint(lo, hi) for _ in range(n)]
            print("Generated Sample Data:", data[:20], "...")

        elif choice == '3':
            if not data:
                print("No data available. Generate or enter numbers first.")
                continue
            res = timed_run(bubble_sort, data)
            print("Sorted:", res["sorted"])
            print("Steps:", res["steps"], "Time (s):", res["time"])

        elif choice == '4':
            if not data:
                print("No data available.")
                continue
            res = timed_run(merge_sort, data)
            print("Sorted:", res["sorted"])
            print("Steps:", res["steps"], "Time (s):", res["time"])

        elif choice == '5':
            if not data:
                print("No data available.")
                continue
            res = timed_run(quick_sort, data)
            print("Sorted:", res["sorted"])
            print("Steps:", res["steps"], "Time (s):", res["time"])

        elif choice == '6':
            if not data:
                print("No data available.")
                continue
            results = {
                "Bubble": timed_run(bubble_sort, data),
                "Merge": timed_run(merge_sort, data),
                "Quick": timed_run(quick_sort, data),
            }
            print_table(results, data)

        elif choice == '7':
            print("Exiting Program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
