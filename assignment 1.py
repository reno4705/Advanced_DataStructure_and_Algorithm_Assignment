def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to optimize the algorithm by detecting if any swaps are made
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swaps are made in an iteration, the array is already sorted
        if not swapped:
            break

# Input array
arr = [5, 2, 9, 1, 5, 6]

# Apply Bubble Sort
bubble_sort(arr)

# Output the sorted array
print("Sorted Array:", arr)

# Sorted Array: [1, 2, 5, 5, 6, 9]
