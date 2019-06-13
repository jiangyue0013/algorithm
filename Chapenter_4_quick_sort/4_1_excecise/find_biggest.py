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


list = [1, 5, 3, 2]
print(find_biggest(list))
