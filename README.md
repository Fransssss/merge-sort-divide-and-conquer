# Merge Sort — Divide and Conquer Demonstration

This lightweight CLI demo animates how merge sort uses Divide and Conquer: the sample list is split, each half is solved, and the results are merged back together so you can see the full recursive story in real time.

## Video Demo
<video src="MergeSortDivideConquer.mp4" controls width="640">
	Your browser does not support embedded videos.
</video>

If the video does not play inline, download it directly from [MergeSortDivideConquer.mp4](MergeSortDivideConquer.mp4) in this repository.

## Divide and Conquer Paradigm
- **Divide:** Break the original problem into smaller subproblems of the same type.
- **Conquer:** Solve each subproblem independently. In merge sort, this means treating single-element lists as already sorted.
- **Combine:** Merge or otherwise recombine the solved subproblems into the final answer.

## Merge Sort in a Nutshell
Merge sort is a stable, comparison-based sorting algorithm that splits a list in half, recursively sorts each half, and then merges the halves in order. Because every level of recursion works on evenly divided halves, merge sort maintains predictable performance regardless of initial order.

## Step-by-Step Algorithm
1. **Divide:** Recursively split the list in half until each sub-list has one element.
2. **Conquer:** Treat the single-element lists as sorted; no further action is required for them.
3. **Combine:** Merge adjacent sorted lists by repeatedly selecting the smallest front element until one sorted list remains.

The console output from `merge_sort.py` logs each divide, conquer, and combine step so you can trace how the recursion unfolds.

## Complexity Analysis
- **Time Complexity:** $O(n \log n)$ because the list is split in half ($\log n$ levels) and each level processes all $n$ elements during merging.
- **Space Complexity:** $O(n)$ additional space is required to hold the temporary merged lists during the combine phase.

## Example
- **Input:** `[34, 7, 23, 32, 5, 62, 78, 12]`
- **Output:** `[5, 7, 12, 23, 32, 34, 62, 78]`

Run `python main.py` to see the detailed divide-and-conquer trace followed by the sorted output.