def findSmallest(arr):  # 用于查找出数组中最小的元素，返回最小元素的索引。
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def select_sort(arr):
    newArr = []
    while arr:
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


arr = [1, 5, 7, 4]
newArr = select_sort(arr)
print(newArr)