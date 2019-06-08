# 阶乘函数
def fact(x):
    if x == 1:  # 基线条件
        return 1
    else:  # 递归条件
        return x * fact(x-1)


if __name__ == '__main__':
    x = 5
    print(fact(x))
