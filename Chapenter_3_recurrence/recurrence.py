# countdown函数
def countdown(i):
    print(i)
    if i <= 1:  # 基线条件
        return
    else:  # 递归条件
        countdown(i-1)


if __name__ == '__main__':
    i = 10
    countdown(i)