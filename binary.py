Binary search is an efficient algorithm for finding a target value within a sorted array. 
It works by repeatedly dividing the search interval in half.
At each step, it compares the target value with the middle element of the array.
If the target value matches the middle element, the search is successful. If the target value is less than the middle element,
the search continues in the lower half of the array. If the target value is greater than the middle element, the search continues in the upper half of the array.
This process is repeated until the target value is found or the search interval is empty.
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # If target is not found in the array
    return -1

# Example usage
arr = [2, 3, 5, 7, 9, 11, 13]
target = 9
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} is present at index {result}")
else:
    print("Element is not present in the array")
