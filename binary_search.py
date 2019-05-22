def binary_search(list, item):
    low =  0
    high = len(list)
    while low <= high:
        mid = int((low + high) / 2 + 0.5)  # 为了实现四舍五入加上一个0.5
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid - 1
    return None

list = [1, 2, 3, 4, 5]
item = 1
position = binary_search(list, item)
print(position)