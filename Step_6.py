import random
import matplotlib.pyplot as plt

# ---------- draw() is now shared by all algorithms ----------

def make_drawer(arr, title, n):
    plt.figure(figsize=(8, 5))

    def draw(highlight_indices=None, pivot_idx=None, sorted_boundary=0, pause_time=0.15):
        plt.clf()
        colors = ["#4C72B0"] * n

        for k in range(sorted_boundary):
            colors[k] = "#55AA55"

        if highlight_indices:
            for idx in highlight_indices:
                colors[idx] = "#DD5555"

        if pivot_idx is not None:
            colors[pivot_idx] = "#E8B93A"

        plt.bar(range(n), arr, color=colors)
        plt.title(title)
        plt.pause(pause_time)

    return draw


# ---------- Algorithms (same logic as Steps 2-5, using shared draw) ----------

def bubble_sort(arr, draw):
    n = len(arr)
    draw(); plt.pause(1)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            draw(highlight_indices=[j, j + 1])
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                draw(highlight_indices=[j, j + 1])
        if not swapped:
            break


def selection_sort(arr, draw):
    n = len(arr)
    draw(); plt.pause(1)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw(highlight_indices=[min_idx, j], sorted_boundary=i)
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            draw(highlight_indices=[i, min_idx], sorted_boundary=i)


def merge_sort(arr, draw):
    n = len(arr)

    def merge(lo, mid, hi):
        left = arr[lo:mid + 1]
        right = arr[mid + 1:hi + 1]
        i = j = 0
        k = lo
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]; i += 1
            else:
                arr[k] = right[j]; j += 1
            k += 1
            draw(highlight_indices=list(range(lo, hi + 1)))
        while i < len(left):
            arr[k] = left[i]; i += 1; k += 1
            draw(highlight_indices=list(range(lo, hi + 1)))
        while j < len(right):
            arr[k] = right[j]; j += 1; k += 1
            draw(highlight_indices=list(range(lo, hi + 1)))

    def sort(lo, hi):
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        sort(lo, mid)
        sort(mid + 1, hi)
        merge(lo, mid, hi)

    draw(); plt.pause(1)
    sort(0, n - 1)


def quick_sort(arr, draw):
    n = len(arr)

    def partition(lo, hi):
        pivot = arr[hi]
        i = lo - 1
        for j in range(lo, hi):
            draw(highlight_indices=[j, hi], pivot_idx=hi)
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                draw(highlight_indices=[i, j], pivot_idx=hi)
        arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
        draw(pivot_idx=i + 1)
        return i + 1

    def sort(lo, hi):
        if lo < hi:
            p = partition(lo, hi)
            sort(lo, p - 1)
            sort(p + 1, hi)

    draw(); plt.pause(1)
    sort(0, n - 1)


# ---------- Menu ----------

ALGORITHMS = {
    "1": ("Bubble Sort", bubble_sort),
    "2": ("Selection Sort", selection_sort),
    "3": ("Merge Sort", merge_sort),
    "4": ("Quick Sort", quick_sort),
}


def main():
    print("=== DSA Visualizer ===")
    print("Choose an algorithm to visualize:")
    for key, (name, _) in ALGORITHMS.items():
        print(f"  {key}. {name}")

    choice = input("Enter choice (1-4): ").strip()

    if choice not in ALGORITHMS:
        print("Invalid choice. Exiting.")
        return

    name, func = ALGORITHMS[choice]

    size_input = input("Array size (press Enter for default 10): ").strip()
    n = int(size_input) if size_input else 10
    arr = [random.randint(1, 50) for _ in range(n)]

    print(f"Running {name} on: {arr}")

    draw = make_drawer(arr, name, n)
    func(arr, draw)

    draw()
    plt.title(f"{name} - Sorted!")
    plt.show()


if __name__ == "__main__":
    main()