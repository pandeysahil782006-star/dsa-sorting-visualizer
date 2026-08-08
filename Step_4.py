import matplotlib.pyplot as plt

CALL_COUNT = 0  # just to slow things down sensibly for very small arrays


def merge_sort_visual(arr, pause_time=0.1):
    n = len(arr)
    plt.figure(figsize=(8, 5))

    def draw(highlight_range=None):
        plt.clf()
        colors = ["#4C72B0"] * n
        if highlight_range:
            lo, hi = highlight_range
            for k in range(lo, hi + 1):
                colors[k] = "#DD5555"
        plt.bar(range(n), arr, color=colors)
        plt.title("Merge Sort Visualizer")
        plt.pause(pause_time)

    def merge(lo, mid, hi):
        # arr[lo..mid] and arr[mid+1..hi] are already individually sorted.
        # We merge them into one sorted block, directly inside arr.
        left = arr[lo:mid + 1]
        right = arr[mid + 1:hi + 1]

        i = j = 0
        k = lo

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            draw(highlight_range=(lo, hi))

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            draw(highlight_range=(lo, hi))

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            draw(highlight_range=(lo, hi))

    def sort(lo, hi):
        if lo >= hi:
            return  # base case: a single element is already "sorted"

        mid = (lo + hi) // 2
        sort(lo, mid)        # sort left half
        sort(mid + 1, hi)    # sort right half
        merge(lo, mid, hi)   # merge the two sorted halves

    draw()
    plt.pause(1)

    sort(0, n - 1)

    draw()
    plt.title("Merge Sort Visualizer - Sorted!")
    plt.show()


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6, 8, 3]
    merge_sort_visual(sample)