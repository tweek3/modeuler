from bisect import bisect
from functools import reduce
from itertools import takewhile, chain
from math import sqrt, factorial, ceil
from operator import mul as omul
from typing import Iterable

from modeuler.itertools import distinct
from modeuler.placeholder import holdable, __, not_


def sqrt_ceil(n):
	"""
	>>> sqrt(25.0)
	5.0
	"""
	return int(ceil(sqrt(n)))


@holdable
def divisors(num: int) -> Iterable[int]:
	"""
	>>> sorted(divisors(24))
	[1, 2, 3, 4, 6, 8, 12]
	"""
	yield 1
	for i in filter(not_(num % __), range(2, sqrt_ceil(num))):
		yield i
		d = num // i
		if d != i:
			yield d


@holdable
def isprime_old(n: int) -> bool:
	"""
	>>> all(map(isprime_old,[5,17,19,67]))
	True
	>>> all(map(isprime,[1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151]))
	True
	>>> any(map(isprime_old,[6,154,256,323]))
	False
	"""
	if n < 2 or n % 2 == 0:
		return False
	return all(map(n % __, range(3, sqrt_ceil(n), 2)))


@holdable
def isprime(n: int) -> bool:
	"""
	>>> all(map(isprime,[5,17,19,67]))
	True
	>>> all(map(isprime,[1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151]))
	True
	>>> any(map(isprime,[6,154,256,323]))
	False
	"""
	it = iterprimes()
	it = takewhile(sqrt_ceil(n) > __, it)
	it = map(n % __, it)
	res = all(it)
	return res


@holdable
def isprime_sieve(sieve, n):
	"""
	>>> all(map(isprime,[5,17,19,67]))
	True
	>>> all(map(isprime,[1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151]))
	True
	>>> any(map(isprime,[6,154,256,323]))
	False
	"""
	return all(map(n % __, takewhile(sqrt_ceil(n) > __, sieve)))


@holdable
def aristo(n):
	s = int(sqrt(n))
	return distinct(range(2, n), trs=lambda x: map(x * __, range(2, s)))


SIEVE = [3]


def _primes(n):
	if n < len(SIEVE):
		return SIEVE[bisect(SIEVE, n)] == n
	return isprime_sieve(SIEVE, n)


@holdable
def iterprimes():
	"""
	>>> import itertools as it
	>>> list(it.islice(iterprimes(),190,200))
	[1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151]
	"""
	yield 2
	i, n = 0, 3
	while True:
		if i == len(SIEVE):
			n += 2
			if _primes(n):
				yield n
				i += 1
				SIEVE.append(n)
		else:
			n = SIEVE[i]
			yield n
			i += 1


@holdable
def concat_digit(a, b, n):
	"""
	>>> concat_digit(45,48,2)
	4548
	"""
	return a * 10 ** n + b


@holdable
def split_digit(n):
	"""
	>>> list(split_digit(78956))
	[7, 8, 9, 5, 6]
	"""
	l = []
	while n > 0:
		l.append(n % 10)
		n //= 10
	l.reverse()
	return l


@holdable
def reversed_split_digit(n):
	"""
	>>> list(reversed_split_digit(78956))
	[6, 5, 9, 8, 7]
	"""
	while n > 0:
		yield n % 10
		n //= 10


@holdable
def circle_permutations(c):
	d = tuple(chain(c, c[:-1]))
	l = len(c)
	for i in range(l):
		yield d[i:i + l]


@holdable
def ispal(num):
	"""
	>>> ispal(78587)
	True
	>>> ispal(7557)
	True
	>>> ispal(58986)
	False
	"""
	s = str(num)
	return s[0:len(s)//2] == s[-1:-(len(s)//2)-1:-1]


@holdable
def isbouncy(n):
	it = iter(str(n))
	last = next(it)
	inc = dec = True
	for d in it:
		inc &= d >= last
		dec &= d <= last
		if not (inc or dec):
			return True
		last = d
	return False


@holdable
def combi(k, n):
	return factorial(n) // factorial(k) * factorial(n - k)


@holdable
def prod(it):
	"""
	>>> prod([1,2,3])
	6
	"""
	return reduce(omul, it)


@holdable
def enum_power(it):
	"""
	>>> list(enum_power(map(10 ** __,range(5))))
	[(1, 1), (10, 10), (100, 100), (1000, 1000), (10000, 10000)]
	"""
	d = 1
	for i in it:
		if d < i:
			d *= 10
		yield i, d
