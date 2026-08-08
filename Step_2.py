import matplotlib.pyplot as plt


def bubble_sort_visual(arr, pause_time=0.15):
    n = len(arr)

    plt.figure(figsize=(8, 5))

    def draw(highlight_indices=None):
        """Redraw the current state of arr as a bar chart.
        highlight_indices: the two bars currently being compared/swapped
        (we colour them differently so it's easy to see what's happening).
        """
        plt.clf()  
        colors = ["#4C72B0"] * n 

        if highlight_indices:
            for idx in highlight_indices:
                colors[idx] = "#DD5555"  
        plt.bar(range(n), arr, color=colors)  # step 1 concept: draw bars
        plt.title("Bubble Sort Visualizer")
        plt.pause(pause_time)  # step 2 concept: pause so we can see this frame

    draw()  # show the initial unsorted array first
    plt.pause(1)  # extra pause at the start so you can see the "before" state

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            draw(highlight_indices=[j, j + 1])  # show which bars we're comparing

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                draw(highlight_indices=[j, j + 1])  # show the result after swap

        if not swapped:
            break

    draw()  # final sorted state
    plt.title("Bubble Sort Visualizer - Sorted!")
    plt.show()  # keep the final window open


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6, 8, 3]
    bubble_sort_visual(sample)