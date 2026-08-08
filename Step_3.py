import matplotlib.pyplot as plt


def selection_sort_visual(arr, pause_time=0.15):
    n = len(arr)
    plt.figure(figsize=(8, 5))

    def draw(highlight_indices=None, sorted_boundary=0):
        plt.clf()
        colors = ["#4C72B0"] * n

        # everything before sorted_boundary is already in final position
        for k in range(sorted_boundary):
            colors[k] = "#55AA55"  # green = confirmed sorted

        if highlight_indices:
            for idx in highlight_indices:
                colors[idx] = "#DD5555"  # red = currently comparing/swapping

        plt.bar(range(n), arr, color=colors)
        plt.title("Selection Sort Visualizer")
        plt.pause(pause_time)

    draw()
    plt.pause(1)

    for i in range(n):
        min_idx = i  # assume current position holds the minimum, for now

        for j in range(i + 1, n):
            draw(highlight_indices=[min_idx, j], sorted_boundary=i)

            if arr[j] < arr[min_idx]:
                min_idx = j  # found a new minimum candidate

        # after scanning the unsorted part, swap the minimum into position i
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            draw(highlight_indices=[i, min_idx], sorted_boundary=i)

    draw(sorted_boundary=n)
    plt.title("Selection Sort Visualizer - Sorted!")
    plt.show()


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6, 8, 3]
    selection_sort_visual(sample)