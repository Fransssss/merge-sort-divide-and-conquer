"""
main.py – Entry point for the Merge Sort / Divide and Conquer demonstration.

Run this file to see Merge Sort in action:
    python main.py
"""

from merge_sort import merge_sort


def main():
    # Example input list
    unsorted_list = [34, 7, 23, 32, 5, 62, 78, 12]

    print("=" * 55)
    print("   Merge Sort – Divide and Conquer Demonstration")
    print("=" * 55)
    print(f"\nOriginal list : {unsorted_list}\n")
    print("-" * 55)
    print("Step-by-step divide and merge trace:\n")

    sorted_list = merge_sort(unsorted_list)

    print("-" * 55)
    print(f"\nSorted list   : {sorted_list}")
    print("=" * 55)


if __name__ == "__main__":
    main()
