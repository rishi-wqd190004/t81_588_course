# two pointer technique with Binary search

## Logic:
# Initialize with left = 0 and right n-1 (last value of list from right)
# run a loop while left < right

# Reference: https://www.geeksforgeeks.org/two-pointers-technique/

def two_sum(arr, target):
    arr.sort()
    left, right = 0, len(arr)-1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1
    return False

arr = [0,-1,2,-3,1]
target = -2
