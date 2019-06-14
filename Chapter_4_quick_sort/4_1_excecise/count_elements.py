def count_elements(list):
    if not list:
        return None
    elif len(list) == 1:
        return 1
    else:
        return 1 + count_elements(list[1:])


list = [1, 2, 3]
print(count_elements(list))
