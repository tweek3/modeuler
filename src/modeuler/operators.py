
import operator
from functools import partial,reduce
import sys


def pam(functions): 
    return partial(reduce,lambda x,f:f(x),functions)

def o(*functions): 
    l = len(functions)
    if l == 0: return lambda x:x
    if l == 1: return functions[0]
    return partial(reduce,lambda x,f:f(x),reversed(functions))

def isoperator(n):
    return not n.startswith('__') and hasattr(getattr(operator,n),'__call__')



sys.modules[__name__].__all__ = list(filter(isoperator,operator.__dict__))
sys.modules[__name__].__dict__.update((n,partial(partial,getattr(operator,n))) for n in filter(isoperator,operator.__dict__))
