import operator
import sys
from functools import partial


def isoperator(n):
    return not n.startswith('__') and hasattr(getattr(operator, n), '__call__')

sys.modules[__name__].__all__ = list(filter(isoperator, operator.__dict__))
sys.modules[__name__].__dict__.update(
        (n, partial(partial, getattr(operator, n))) for n in filter(isoperator, operator.__dict__))








