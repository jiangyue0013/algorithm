def bubble_sort(numberlist):
    length = len(numberlist)
    for i in range(length):
        for j in range(1, length - i):
            if numberlist[j - 1] > numberlist[j]:
                numberlist[j], numberlist[j - 1] = numberlist[j - 1], numberlist[j]
    return numberlist


data_test=[10,23,1,53,654,54,16,646,65,3155,546,31]
sorted_list = bubble_sort(data_test)
print(sorted_list)