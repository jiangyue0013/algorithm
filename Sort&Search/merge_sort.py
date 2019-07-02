def  merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


def merge_sort(numberlist):
    if len(numberlist) <= 1:
        return numberlist
    mid = len(numberlist) // 2
    left = numberlist[:mid]
    right = numberlist[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


test = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
print("Original:", test)
print('Sorted:', merge_sort(test))