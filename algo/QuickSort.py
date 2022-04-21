"""Quick Sort avg time O(nlogn) worst O(n^2), space O(logn)"""
# Function to perform quicksort
def quickSort(array, low, high):
  if low < high:
 
    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)
 
    # Recursive call on the left of pivot
    quickSort(array, low, pi - 1)
 
    # Recursive call on the right of pivot
    quickSort(array, pi + 1, high)

"""Partition with last element as pivot"""
def partition(array, low, high):
  pivot = array[high]
 
  # Pointer for greater element
  i = low - 1
 
  # Traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
 
      # Swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
 
  # Swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
 
  # Return the position from where partition is done
  return i + 1
 


arr = [1,61,17,8,2,91,99,83]
quickSort(arr, 0, len(arr)-1)
print(arr)
arr = [1,61,17,8,2,91,99,83,22]
quickSort(arr, 0, len(arr)-1)
print(arr)