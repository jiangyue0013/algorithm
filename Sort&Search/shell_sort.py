def shell_sort(numberlist):
    length = len(numberlist)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            print(i)
            temp = numberlist[i]
            j = i
            while j >= gap and numberlist[j - gap] > temp:
                numberlist[j] = numberlist[j - gap]
                j -= gap
            numberlist[j] = temp
        gap = gap // 2
    return numberlist

numberlist = [10, 14, 73, 25, 23, 13, 27, 94, 33, 39, 25, 59, 94, 65, 82, 45]
print(shell_sort(numberlist))