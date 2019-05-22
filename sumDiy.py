def factorial(n):
    if  n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))

def qiuhe(arr):
    if len(arr) > 1:
        return arr[0] + qiuhe(arr.pop(0))
    else:
        return arr[0]

arr = [1, 2, 3]
print(len(arr))
# print(qiuhe(arr))