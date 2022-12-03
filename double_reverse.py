import timeit


def double_reverse() -> int:
    num = int(input())
    while not num % 10:
        num //= 10
    result = sum([i for i in range(1, num + 1)]) % (10 ** 9 + 7)
    return result


print(double_reverse())
# print(timeit.timeit(stmt=double_reverse, number=25))
