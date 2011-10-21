from itertools import starmap

def tonum(t):
    return sum(starmap(lambda i,x: x*10**i, enumerate(reversed(t))))


def binomial_contains(func,n,min,max):
    while min < max-1: 
        index = min+(max-min)//2
        res = func(index)
        if res == n: 
            return True 
        if res > n: 
            max=index
        else:
            min=index
        
    return False

