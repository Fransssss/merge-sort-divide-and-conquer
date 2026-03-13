"""Entry point for demonstrating Merge Sort using Divide and Conquer."""
from merge_sort import merge_sort

def main() -> None:
    """Run the merge sort demonstration on a sample list."""
    numbers = [34, 7, 23, 32, 5, 62, 78, 12]
    print("Original list:", numbers)
    print("\n--- Merge Sort Trace ---")
    sorted_numbers = merge_sort(numbers)
    print("\nSorted list:", sorted_numbers,'\n')

if __name__ == "__main__":
    main()
