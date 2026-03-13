def merge_sort(lst):
    """
    Sorts a list using the Merge Sort algorithm.

    This function demonstrates the Divide and Conquer paradigm:
      1. Divide   - split the list into two halves
      2. Conquer  - recursively sort each half
      3. Combine  - merge the two sorted halves into one sorted list

    Args:
        lst (list): The unsorted list of comparable elements.

    Returns:
        list: A new sorted list.
    """

    # Base case: a list of 0 or 1 elements is already sorted
    if len(lst) <= 1:
        return lst

    # ── DIVIDE ────────────────────────────────────────────────────────────────
    # Find the midpoint and split the list into left and right halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    print(f"Dividing : {lst}")
    print(f"  Left   : {left_half}")
    print(f"  Right  : {right_half}")

    # ── CONQUER ───────────────────────────────────────────────────────────────
    # Recursively sort each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # ── COMBINE ───────────────────────────────────────────────────────────────
    # Merge the two sorted halves and return the result
    merged = _merge(sorted_left, sorted_right)
    print(f"Merging  : {sorted_left} + {sorted_right} -> {merged}")
    return merged


def _merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left  (list): A sorted list.
        right (list): A sorted list.

    Returns:
        list: A single sorted list containing all elements from both inputs.
    """
    result = []
    i = 0  # pointer for left list
    j = 0  # pointer for right list

    # Compare elements from both lists one by one and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from either list
    result.extend(left[i:])
    result.extend(right[j:])

    return result
