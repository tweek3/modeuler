import operator as op
from functools import wraps, reduce, partial
from itertools import islice
from typing import Callable, Any, Tuple

from modeuler.type_alias import A, B, Fn, It


def is_placeholder(obj) -> bool:
	return isinstance(obj, Placeholder)


def apply(x, f):
	return f(x)


class Placeholder(object):
	"""
	>>> list(map(2 ** __, range(4)))
	[1, 2, 4, 8]
	>>> list(map(__ ** 2, range(4)))
	[0, 1, 4, 9]
	>>> (__ + 2)(1)
	3
	>>> (3 + __)(1)
	4
	>>> (4 + __ + 5)(1)
	10
	>>> (__ + __)(1,5)
	6
	>>> (__ + 4 + __)(1,5)
	10
	>>> range(__, __)(1,2)
	range(1, 2)
	>>> not_(truth(range(__, __))) (1,2)
	False
	>>> truth(__ == 1)(1)
	True
	>>> len_(__[:5])(range(10))
	5
	>>> ~ __ (1) == ~ 1
	True
	>>> (__ << __)(4,1)
	8
	"""
	def __init__(self, fn, size):
		self.fn = fn
		self.size = size

	def __call__(self, *args):
		return self.fn(*args)


def apply_all(ita: It[A], itb: It[B]) -> It:
	"""
	>>> from itertools import repeat
	>>> list(apply_all([1,Placeholder(op.add,2),3,Placeholder(op.neg,1),4], repeat(1)))
	[1, 2, 3, -1, 4]
	"""
	ita, itb = iter(ita), iter(itb)
	for a in ita:
		if is_placeholder(a):
			if a.size == 1:
				yield a.fn(next(itb))
			elif a.size == 2:
				yield a.fn(next(itb), next(itb))
			else:
				yield a.fn(*tuple(islice(itb, a.size)))
		else:
			yield a


def holdable(fn: Callable):
	"""
	>>> holdable(op.add)(__,2)(3)
	5
	>>> holdable(lambda x, y: x + y)(__, __)(1, 2)
	3
	>>> holdable(lambda x, y ,z: x + y + z)(__, __, 3)(__, 2)(1)
	6
	"""

	@wraps(fn)
	def wraper(*args):
		holders = list(filter(is_placeholder, args))
		if not holders:
			return fn(*args)

		if len(args) == 1:
			return Placeholder(lambda *x: fn(args[0].fn(*x)), args[0].size)

		def func(*sub_args):
			new_args = tuple(apply_all(args, sub_args))
			return fn(*new_args)

		return Placeholder(func, sum(h.size for h in holders))

	return wraper


def _op_revop(fn: Callable[[Any, Any], Any]) -> Tuple[Placeholder, Placeholder]:
	return holdable(fn), holdable(lambda x, y: fn(y, x))

Placeholder.__add__, Placeholder.__radd__ = _op_revop(lambda a, b: a + b)
Placeholder.__sub__, Placeholder.__rsub__ = _op_revop(op.sub)
Placeholder.__mul__, Placeholder.__rmul__ = _op_revop(op.mul)
Placeholder.__mod__, Placeholder.__rmod__ = _op_revop(lambda a, b: a % b)
Placeholder.__pow__, Placeholder.__rpow__ = _op_revop(op.pow)
Placeholder.__and__, Placeholder.__rand__ = _op_revop(op.and_)
Placeholder.__xor__, Placeholder.__rxor__ = _op_revop(op.xor)
Placeholder.__or__, Placeholder.__ror__ = _op_revop(op.or_)
Placeholder.__truediv__, Placeholder.__rtruediv__ = _op_revop(op.truediv)
Placeholder.__floordiv__, Placeholder.__rfloordiv__ = _op_revop(op.floordiv)
Placeholder.__divmod__, Placeholder.__rdivmod__ = _op_revop(divmod)
Placeholder.__matmul__, Placeholder.__rmatmul__ = _op_revop(op.matmul)
Placeholder.__rshift__, Placeholder.__rrshift__ = _op_revop(op.rshift)
Placeholder.__lshift__, Placeholder.__rlshift__ = _op_revop(op.lshift)
Placeholder.__lshift__, Placeholder.__rlshift__ = _op_revop(op.lshift)

Placeholder.__neg__ = holdable(op.neg)
Placeholder.__invert__ = holdable(op.invert)
Placeholder.__abs__ = holdable(op.abs)
Placeholder.__pos__ = holdable(op.pos)
Placeholder.__eq__ = holdable(op.eq)
Placeholder.__lt__ = holdable(op.lt)
Placeholder.__le__ = holdable(op.le)
Placeholder.__gt__ = holdable(op.gt)
Placeholder.__ge__ = holdable(op.ge)

Placeholder.__getitem__ = holdable(op.getitem)
Placeholder.__str__ = holdable(str)
Placeholder.__contains__ = holdable(op.contains)

len_ = holdable(len)
truth = holdable(bool)
not_ = holdable(op.not_)
is_ = holdable(op.is_)
is_not = holdable(op.is_not)
range = holdable(range)
contains = holdable(op.contains)
in_ = holdable(op.contains)
__ = Placeholder(lambda x: x, 1)


def pam(functions: It[Fn]):
	"""
	>>> pam([__ + 2, 3 * __])(1)
	9
	"""
	return partial(reduce, lambda x, f: f(x), functions)


def o(*functions: Fn):
	"""
	>>> o(__ + 2, 3 * __)(1)
	5
	"""
	l = len(functions)
	if l == 0:
		return lambda x: x
	if l == 1:
		return functions[0]
	return partial(reduce, lambda x, f: f(x), reversed(functions))
