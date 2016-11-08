from math import sqrt
from itertools import count
from modeuler.maths import sqrt_ceil
from math import ceil

squares = {d*d for d in range(2, 1001)}
D = [d for d in range(2, 1001) if d not in squares]


def is_diophan(x,y,d) -> bool:
    return x*x - d*y*y == 1


def is_diosquare(x2,y2,d) -> bool:
    return x2 - d*y2 == 1


def findx2(d):
    for y in count(2):
        res = d*y*y+1
        if res in squares:
            return res
        if res < 1000000:
            continue
        rt = sqrt(res)
        if ceil(rt) == rt:
            return res

def findx(d):
    for y in range(2, d):
        pass


def listx2():
    for d in range(2, 101):
        if d not in squares:
            yield findx2(d)

print(findx(7))

# for s in map(lambda x: x*x, count(2)):
#     pass
