# Binary search is an efficient algorithm for finding a target value within a sorted array. 
# It works by repeatedly dividing the search interval in half.
# At each step, it compares the target value with the middle element of the array.
# If the target value matches the middle element, the search is successful. If the target value is less than the middle element,
# the search continues in the lower half of the array. If the target value is greater than the middle element, the search continues in the upper half of the array.
# This process is repeated until the target value is found or the search interval is empty.

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



arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 14
Initial State:
The array is sorted: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].
left = 0 (index of the first element), right = 9 (index of the last element).
Iteration 1:
Calculate mid = (left + right) // 2 = (0 + 9) // 2 = 4.
Compare arr[4] (which is 10) with the target (14). Since 10 < 14, we update left = mid + 1 = 5.
Iteration 2:
Calculate mid = (left + right) // 2 = (5 + 9) // 2 = 7.
Compare arr[7] (which is 16) with the target (14). Since 16 > 14, we update right = mid - 1 = 6.
Iteration 3:
Calculate mid = (left + right) // 2 = (5 + 6) // 2 = 5.
Compare arr[5] (which is 12) with the target (14). Since 12 < 14, we update left = mid + 1 = 6.
Iteration 4:
Calculate mid = (left + right) // 2 = (6 + 6) // 2 = 6.
Compare arr[6] (which is 14) with the target (14). Since 14 equals the target, the search is successful, and we return the index 6.
