"""Merge Sort worst and avg O(nlogn) time, O(n) space"""
def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements into 2 halfs and sort each
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        print(f'Before merging {arr} left is {left_arr}, right is {right_arr}', end='\n\n')


        sorted_left = mergeSort(left_arr)
        sorted_right = mergeSort(right_arr)
        print(f'Merging left : {sorted_left}, right: {sorted_right} of {arr}')

        #index of current arr that contains the sorting result
        #index of left arr,
        #index of right arr,
        aindex, lindex, rindex, llen, rlen = 0, 0, 0, len(sorted_left), len(sorted_right)
        while lindex < llen and rindex < rlen:
            if sorted_left[lindex] < sorted_right[rindex]:
                arr[aindex] = sorted_left[lindex]
                lindex += 1
            else:
                arr[aindex] = sorted_right[rindex]
                rindex += 1
            aindex += 1
        
        # Checking if any element was left
        while lindex < llen:
            arr[aindex] = sorted_left[lindex]
            lindex += 1
            aindex+=1
        
        while rindex < rlen:
            arr[aindex] = sorted_right[rindex]
            rindex += 1
            aindex += 1
        
        print(f'Finished merging {arr}', end='\n\n')
        return arr
    else: return arr

arr = [1,61,17,8,2,91,99,83]
print(mergeSort(arr))
arr = [1,61,17,8,2,91,99,83,22]
print(mergeSort(arr))