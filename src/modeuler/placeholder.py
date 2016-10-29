
import functools as ft


def placeholdable(func):
    @ft.wraps
    def wraper(*args,**kvargs):
        h = map(lambda a:isinstance(a,placeholder),args)
        if not h:
            return func(*args,**kvargs)
        def curryf(*args):
            new_args = map


class placeholder:
    pass