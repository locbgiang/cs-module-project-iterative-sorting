def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if target == arr[i]:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    start = 0
    end = len(arr) - 1 
    mid = 0
    while start <= end:
        mid = int((end+start)/2)
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1  # not found

'''
arr = [1,2,3,4,5,6,7,8,9,10]

answer = linear_search(arr, 8)

print(answer)
'''
arr = [1,2,3,4,5,6,7,8,9]
answer = binary_search(arr, 10)
print(answer)