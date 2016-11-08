
from functools import lru_cache


@lru_cache(maxsize=None)
def combi(n, size):
    if size > n or n < 2:
        return 0
    if size == n or size == n - 1:
        return 1
    if size == 2:
        return n // 2

    return sum(combi(n - 1 - i, size - 1) for i in range(0, n - 1, size))

print(sum(combi(1000, i) for i in range(2, 101)))