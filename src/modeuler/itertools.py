from functools import partial, reduce
from itertools import filterfalse,islice
from operator import contains, mul


def rap(func,iterable,init=None):
    it = iter(iterable)
    if init is None:
        init = next(it)
    yield init
    for i in it:
        init = func(init,i)
        yield init 
    
def last(it):
    return reduce(lambda x,y:y,it)

def unique(it,trs=lambda i:[i],on=set()):
    for i in filterfalse(partial(contains,on),it):
        yield i
        for n in trs(i): on.add(n)

def prod(it):
    return reduce(mul,it)

def size(it):
    return reduce(lambda x,y: x+1,it,0)

def iterslice(iterable,size):
    it = iter(iterable)
    mem = list(islice(it,size))
    yield tuple(mem)
    for i in it:
        mem.pop(0)
        mem.append(i)
        yield tuple(mem)
        
def listcycle(li):
    i = 0
    while li:
        if i > len(li): i=0
        yield li[i]
        i+=1
