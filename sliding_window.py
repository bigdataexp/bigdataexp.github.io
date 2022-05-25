# Sliding Window Pattern has following question variations:
# Fixed Length of window and iterable data structure and ask is to find something like max su, min, contains etc.
# Dynamic Length of Window(it can grow and shrink) and from iterable data structure, find a subset with something like sum, max sum, avg, contains, shortest.
# Dynamic Length of Window with a Auxillary data structure.


#First problem with a fixed length of window, find the maxinum sum of continous subarray.

#Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
def max_subarray_with_fixed_size(arr, k):
    
    current_sum = 0
    max_sum = 0

    for i, value in enumerate(arr):
        current_sum += value
        
        if i >= (k-1):
            max_sum = max(current_sum, max_sum)
            current_sum -= arr[i-(k-1)]
            
    print(max_sum)
    
    
    
max_subarray_with_fixed_size([2, 3, 4, 1, 5], 2)
    








