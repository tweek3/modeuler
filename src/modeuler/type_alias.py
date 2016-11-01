
from typing import Iterable, Callable, TypeVar, Union

A, B, C = TypeVar('A'), TypeVar('B'), TypeVar('C')

A_B = Union[A, B]

It = Iterable
Fn = Callable

