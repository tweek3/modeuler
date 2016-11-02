from functools import partial, reduce
from itertools import filterfalse, islice
from operator import contains
from typing import Optional

from modeuler.placeholder import __, holdable
from modeuler.type_alias import A, B, It, Fn


def fmap(fn: Fn[[A], B], container: B) -> B:
	"""
	>>> list(fmap(range, [6, 2]))
	[0, 1, 2, 3, 4, 5, 0, 1]
	>>> list(fmap(__, [[1, 1 ,1], [2], [3]]))
	[1, 1, 1, 2, 3]
	"""
	for e in container:
		yield from fn(e)


def rap(func: Fn[[A, A], B], it: It[A], init: A=None) -> It[B]:
	"""
	>>> list(rap(__ + __, range(5), 1))
	[1, 1, 2, 4, 7, 11]
	"""
	it = iter(it)
	if init is None:
		init = next(it)
	yield init
	for i in it:
		init = func(init, i)
		yield init


@holdable
def last(it: It[A]) -> Optional[A]:
	"""
	>>> last(i for i in range(5))
	4
	>>> print(last([]))
	None
	"""
	sentinel = object()
	it = iter(it)
	first = next(it, sentinel)
	if first is sentinel:
		return None
	return reduce(lambda x, y: y, it, first)


@holdable
def distinct(it: It[A], trs: Fn[[A], bool]=lambda *a: a, on=set())-> It[A]:
	"""
	>>> list(distinct([1,1,1,2,2,3,4,4,4]))
	[1, 2, 3, 4]
	>>> list(distinct([]))
	[]
	"""
	for i in filterfalse(partial(contains, on), it):
		yield i
		on.update(trs(i))


@holdable
def size(it: It)->int:
	"""
	>>> size(range(9))
	9
	>>> size(iter([]))
	0
	"""
	return reduce(lambda x, y: x + 1, it, 0)


def partition(n: int, it: It[A], step: int=0)-> It[It[A]]:
	"""
	>>> list(partition(3,range(7),step=1))
	[(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]

	>>> list(partition(3,range(9)))
	[(0, 1, 2), (3, 4, 5), (6, 7, 8)]

	>>> list(partition(3,[]))
	[]
	"""
	step = step or n
	it = iter(it)
	mem = list(islice(it, n))
	if not mem:
		return
	yield tuple(mem)
	for i, e in enumerate(it, n + 1):
		mem.pop(0)
		mem.append(e)
		if not i % step:
			yield tuple(mem)
