def counting_sort(numberlist, maxnumber):  # maxnumber为数组中的最大值
    length = len(numberlist)  # 待排序数组长度
    b = [0 for i in range(length)] # 设置输出序列，初始化为0
    c = [0 for i in range(length + 1)]  # 设置技术序列，初始化为0
    for j in numberlist:
        c[j] = c[j] + 1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i - 1]
    for j in numberlist:
        b[c[j] - 1] = j
        c[j] = c[j] - 1
    return b


numberlist = [9, 2, 1, 7, 6, 8, 5, 3, 4]
maxnumber = 9
print(counting_sort(numberlist, maxnumber))