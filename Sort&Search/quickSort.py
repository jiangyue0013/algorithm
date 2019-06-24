def quickSort(array):
    if len(array) < 2:  # 基线条件
        return array
    else:  # 递归条件
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

array = [10, 7, 9 , 3, 3, 2]
newArray = quickSort(array)
print(newArray)
