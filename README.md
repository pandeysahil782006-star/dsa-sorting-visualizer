# DSA Sorting Visualizer

A Python tool that visualizes how classic sorting algorithms work, using live bar-chart animations built with Matplotlib.

## Why this project?

Understanding sorting algorithms from code alone can be hard — this project makes the process visible: you can literally watch elements compare, swap, and settle into sorted order.

## Algorithms Implemented

| Algorithm | Approach | Time Complexity (avg) |
|---|---|---|
| Bubble Sort | Repeated adjacent swaps | O(n²) |
| Selection Sort | Find min, place at front | O(n²) |
| Merge Sort | Divide and conquer | O(n log n) |
| Quick Sort | Pivot-based partitioning | O(n log n) |

## How it works

Each algorithm redraws a bar chart after every meaningful operation (comparison/swap), using matplotlib's `bar()`, `pause()`, and `clf()` to create a simple frame-by-frame animation.

- **Red bars** — elements currently being compared/swapped
- **Yellow bar** — the pivot (Quick Sort only)
- **Green bars** — elements confirmed to be in their final sorted position (Selection Sort)

## Running it

```bash
pip install matplotlib
python3 step6_main.py
```

You'll be asked to choose an algorithm (1-4) and an array size, then a window will open showing the sort happening live.

## Project Structure
step1_bubble_sort.py # plain bubble sort, terminal output only
step2_bubble_sort_visual.py # bubble sort + matplotlib animation
step3_selection_sort_visual.py # selection sort + animation
step4_merge_sort_visual.py # merge sort + animation
step5_quick_sort_visual.py # quick sort + animation
step6_main.py # combined menu - run this one

## What I learned building this

- Matplotlib basics for simple animations (bar, pause, clf)
- How to translate algorithm logic (already known from DSA practice) into a visual, interactive format
- Structuring a small Python project with reusable components (shared `draw()` function across algorithms)

## Author

Sahil Pandey — B.Tech Software Engineering, Delhi Technological University

```

```
