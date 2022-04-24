def find(arr) -> int:
    arrlen = len(arr)
    if arrlen < 1: return 0
    if arrlen == 1: return 1 if arr[0] % 2 else 0
    if arrlen == 2:
        a0 = 1 if arr[0] % 2 else 0
        a1 = 1 if arr[1] % 2 else 0
        return a0 + a1
    mid = arrlen // 2
    cur = 1 if arr[mid] % 2 else 0
    return cur + find(arr[:mid]) + find(arr[mid+1:])


arr = [1,2,3,4,7,8,11]
print(find(arr))
arr = [1,3,5,7,9]
print(find(arr))
