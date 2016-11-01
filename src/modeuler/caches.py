from functools import wraps


def cache(func):
    _cache = {}

    @wraps(func)
    def _func(*args, **kwargs):
        tmp = _cache.get(args, None)
        if tmp:
            return tmp
        return _cache.setdefault(args, func(*args, **kwargs))

    return _func
