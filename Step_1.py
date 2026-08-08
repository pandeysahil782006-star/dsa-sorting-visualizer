"""
DSA Visualizer - Step 1
------------------------
Goal: Plain bubble sort, but after every SWAP we print the current
state of the array. No matplotlib yet - just terminal output.
"""

def bubble_sort(arr):
    n = len(arr)
    step = 0  # counts how many swaps have happened so far

    for i in range(n):
        swapped = False  # optimization: if no swap happens in a full pass, array is sorted

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                step += 1

                # this is our "visualization" for now - just print the state
                print(f"Step {step}: swapped index {j} and {j+1} -> {arr}")

        if not swapped:
            # array is already sorted, no need to keep looping
            print("No swaps in this pass -> array is sorted, breaking early.")
            break

    return arr


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print("Original array:", sample)
    print("-" * 50)

    sorted_arr = bubble_sort(sample)

    print("-" * 50)
    print("Final sorted array:", sorted_arr)
