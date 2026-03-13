# merge-sort-divide-and-conquer

A beginner-friendly Python project that demonstrates the **Divide and Conquer** algorithm paradigm through **Merge Sort**.

---

## Divide and Conquer Paradigm

**Divide and Conquer** is a problem-solving strategy that works in three steps:

| Step    | Description |
|---------|-------------|
| **Divide**  | Break the problem into smaller sub-problems of the same type. |
| **Conquer** | Solve each sub-problem recursively (base case: a problem small enough to solve directly). |
| **Combine** | Merge the solutions of the sub-problems to produce the solution to the original problem. |

---

## Merge Sort

**Merge Sort** is a classic sorting algorithm that applies the Divide and Conquer strategy:

1. **Divide** – Split the unsorted list into two roughly equal halves.
2. **Conquer** – Recursively sort each half.
3. **Combine** – Merge the two sorted halves into one sorted list.

Because the merge step always produces a correctly sorted result, the algorithm is guaranteed to sort the entire list once all recursive calls return.

---

## Project Structure

```
merge-sort-divide-and-conquer/
├── main.py        # Entry point – runs the demonstration
├── merge_sort.py  # Merge Sort implementation with step-by-step trace
└── README.md      # This file
```

---

## Step-by-Step Algorithm Walkthrough

Given the list `[34, 7, 23, 32, 5, 62, 78, 12]`:

```
Step 1 – Divide
  [34, 7, 23, 32, 5, 62, 78, 12]
        /                 \
[34, 7, 23, 32]      [5, 62, 78, 12]

Step 2 – Divide further
  [34, 7, 23, 32]          [5, 62, 78, 12]
     /       \               /        \
 [34, 7]  [23, 32]       [5, 62]   [78, 12]
  /   \     /   \         /   \     /    \
[34] [7] [23] [32]      [5] [62] [78]  [12]

Step 3 – Conquer (base case: single-element lists are already sorted)

Step 4 – Combine (merge back up)
[7, 34]  [23, 32]     [5, 62]  [12, 78]
    \      /               \    /
  [7, 23, 32, 34]       [5, 12, 62, 78]
         \                  /
       [5, 7, 12, 23, 32, 34, 62, 78]
```

---

## Time Complexity

| Case    | Complexity  |
|---------|-------------|
| Best    | O(n log n)  |
| Average | O(n log n)  |
| Worst   | O(n log n)  |

**Why O(n log n)?**
- The list is divided in half at each level → **log n** levels of recursion.
- At each level, merging all elements together takes **O(n)** time.
- Combined: **O(n) × O(log n) = O(n log n)**.

---

## Space Complexity

**O(n)** – Merge Sort requires additional memory proportional to the size of the input list because the merge step creates temporary lists to hold the left and right halves during each merge.

---

## Example Input and Output

**Input:**
```
[34, 7, 23, 32, 5, 62, 78, 12]
```

**Output:**
```
=======================================================
   Merge Sort – Divide and Conquer Demonstration
=======================================================

Original list : [34, 7, 23, 32, 5, 62, 78, 12]

-------------------------------------------------------
Step-by-step divide and merge trace:

Dividing : [34, 7, 23, 32, 5, 62, 78, 12]
  Left   : [34, 7, 23, 32]
  Right  : [5, 62, 78, 12]
...
-------------------------------------------------------

Sorted list   : [5, 7, 12, 23, 32, 34, 62, 78]
=======================================================
```

---

## How to Run

```bash
python main.py
```

Requires **Python 3.6+**. No external dependencies.