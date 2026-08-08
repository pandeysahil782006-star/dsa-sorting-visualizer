import matplotlib.pyplot as plt


def quick_sort_visual(arr, pause_time=0.15):
    n = len(arr)
    plt.figure(figsize=(8, 5))

    def draw(highlight_indices=None, pivot_idx=None):
        plt.clf()
        colors = ["#4C72B0"] * n

        if highlight_indices:
            for idx in highlight_indices:
                colors[idx] = "#DD5555"  # red = comparing

        if pivot_idx is not None:
            colors[pivot_idx] = "#E8B93A"  # yellow = current pivot

        plt.bar(range(n), arr, color=colors)
        plt.title("Quick Sort Visualizer")
        plt.pause(pause_time)

    def partition(lo, hi):
        pivot = arr[hi]  # choosing the last element as pivot
        i = lo - 1  # boundary of "smaller than pivot" region

        for j in range(lo, hi):
            draw(highlight_indices=[j, hi], pivot_idx=hi)

            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                draw(highlight_indices=[i, j], pivot_idx=hi)

        # place the pivot in its correct final position
        arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
        draw(pivot_idx=i + 1)

        return i + 1  # this is the pivot's final sorted index

    def sort(lo, hi):
        if lo < hi:
            pivot_index = partition(lo, hi)
            sort(lo, pivot_index - 1)   # sort left of pivot
            sort(pivot_index + 1, hi)   # sort right of pivot

    draw()
    plt.pause(1)

    sort(0, n - 1)

    draw()
    plt.title("Quick Sort Visualizer - Sorted!")
    plt.show()


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6, 8, 3]
    quick_sort_visual(sample)