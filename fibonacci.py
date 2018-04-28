# coding:utf-8

"""
斐波那契数列/台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
"""


def _a(n):
    if n > 2:
        return _a(n-2)+_a(n-1)
    else:
        return n


def memo(func):
    """记住每个阶级的跳法"""
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)


if __name__ == '__main__':
    a = fib(3)
    print(a)
