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


list = [1, 2, 3, 4, 5]
target = 3
print(binary_search_dc(list, target))