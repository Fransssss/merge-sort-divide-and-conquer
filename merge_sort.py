"""Merge Sort implementation demonstrating the Divide and Conquer paradigm."""
from __future__ import annotations

import time
from typing import List

ANIMATION_FRAMES = "|/-\\"

def _animate_step(message: str, indent: str, duration: float = 0.8, frame_delay: float = 0.2) -> None:
    """Display a small spinner animation so the recursive steps feel paced."""
    end_time = time.perf_counter() + duration
    frame_index = 0
    while time.perf_counter() < end_time:
        frame = ANIMATION_FRAMES[frame_index % len(ANIMATION_FRAMES)]
        print(f"\r{indent}{message} {frame}", end="", flush=True)
        time.sleep(frame_delay)
        frame_index += 1
    print(f"\r{indent}{message} done")

def merge_sort(numbers: List[int], depth: int = 0) -> List[int]:
    """Sort a list of integers using merge sort while printing divide/conquer/combine steps."""
    indent = "  " * depth

    # Conquer: lists of length 0 or 1 are already sorted
    if len(numbers) <= 1:
        _animate_step("Conquer step", indent, duration=0.5)
        print(f"{indent}Conquer: {numbers} is already sorted")
        return numbers.copy()

    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]

    # Divide: split the list into left and right halves
    _animate_step("Dividing list", indent)
    print(f"{indent}Divide: {numbers} -> {left_half} | {right_half}")

    sorted_left = merge_sort(left_half, depth + 1)
    sorted_right = merge_sort(right_half, depth + 1)

    # Combine: merge the sorted halves back together
    _animate_step("Combining halves", indent)
    merged = _merge(sorted_left, sorted_right, depth)
    print(f"{indent}Combine: {sorted_left} + {sorted_right} -> {merged}")
    return merged

def _merge(left: List[int], right: List[int], depth: int) -> List[int]:
    """Merge two sorted lists while logging the conquer step."""
    indent = "  " * depth
    _animate_step("Merging halves", indent)
    print(f"{indent}Conquer: merging {left} and {right}")

    merged: List[int] = []
    left_index = 0
    right_index = 0

    # Merge while both lists have elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left list
    if left_index < len(left):
        merged.extend(left[left_index:])

    # Append any remaining elements from the right list
    if right_index < len(right):
        merged.extend(right[right_index:])

    return merged
