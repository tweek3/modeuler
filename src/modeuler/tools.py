
from modeuler.placeholder import holdable, __
from modeuler.type_alias import It


@holdable
def tonum(t: It[int]):
    """
    >>> tonum([9, 7, 8, 1])
    9781
    >>> tonum([])
    0
    """
    return sum(map(__ * (10 ** __), t, range(len(t)-1, -1, -1)))


@holdable
def binomial_contains(func, n, start, end):
    while start < end - 1:
        index = start + (max - start) // 2
        res = func(index)
        if res == n:
            return True
        if res > n:
            end = index
        else:
            start = index

    return False
