def diy_sum(arr):
    if not arr:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr.pop(0) + diy_sum(arr)


arr = [1, 2, 3]
print(diy_sum(arr))