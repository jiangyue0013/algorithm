'''
快速排序使用分而治之（ D&C ）的策略

D&C(Devide and Conquer)的工作原理
1. 找出简单的基线条件
2. 确定如何缩小问题的规模，使其符合基线条件

快速排序的独特之处在于，其速度取决于选择的基准值。

大O表示法的相关知识
O(n)表示法中的 n 表示语句运行的次数。

小结
D&C将问题逐步分解。使用 D&C 处理列表时，基线条件很可能是空数组或只包含一个元素的数组。
实现快速排序时，请随机地选择用作基准值的元素。快速排序的平均运行时间为O(nlogn)。
大O表示法中的常量有时候事关重大，这就是快速排序比合并排序快的原因所在。
比较简单查找和二分查找时，常量几乎无关紧要，因为列表很长时，O(logn)的速度比O(n)的快得多。
'''
# 快速排序
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# 二分查找
def binary_search_basic(list, target, low, high):
    if low > high:
        return None
    else:
        mid = int((low + high) / 2 + 0.5)
        guess = list[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
            return binary_search_basic(list, target, low, high)
        else:
            low = mid + 1
            return binary_search_basic(list, target, low, high)


def binary_search_dc(list, target):
    return binary_search_basic(list, target, 0, len(list) - 1)


# 
def count_elements(list):
    if not list:
        return None
    elif len(list) == 1:
        return 1
    else:
        return 1 + count_elements(list[1:])


# 数组求和
def diy_sum(arr):
    if not arr:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr.pop(0) + diy_sum(arr)


# 查找列表中的最大值
def bigger(int1, int2):
    if int1 >= int2:
        return int1
    else:
        return int2


def find_biggest(list):
    if not list:
        return None
    elif len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return bigger(list[0], list[1])
    else:
        return bigger(list[0], find_biggest(list[1:]))


if __name__ == "__main__":
    pass