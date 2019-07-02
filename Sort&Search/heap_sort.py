def heap_sort(numberlist):
    length = len(numberlist)
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and numberlist[child] < numberlist[child + 1]:
                child += 1
            if numberlist[root] < numberlist[child]:
                numberlist[root], numberlist[child] = numberlist[child], numberlist[root]
                root = child
            else:
                break
    
# 创建最大堆
    for start in range((length - 2) // 2, -1, -1):
        sift_down(start, length - 1)

# 堆排序
    for end in range(length - 1, 0, -1):
        numberlist[0], numberlist[end] = numberlist[end], numberlist[0]
        sift_down(0, end - 1)
    
    return numberlist


numberlist = [9, 2, 1, 7, 6, 8, 5, 3, 4]
print(heap_sort(numberlist))