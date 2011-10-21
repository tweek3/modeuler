from functools import wraps

def cache(func):
    _cache = {}
    @wraps(func)
    def _func(*args,**kwargs):
        tmp = _cache.get(args,None)
        if tmp: return tmp
        return _cache.setdefault(args,func(*args,**kwargs))
    return _func


def permutation_cache(ret=tuple):
    _cache = {}
    def _dec(func):
        @wraps(func)
        def _func(c):
            tmp = _cache.get(c,None)
            if tmp: return tmp
            tmp=func(c)
            for n in tmp:
                _cache[n] = tmp
            return tmp
        return 