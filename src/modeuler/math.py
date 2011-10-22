from itertools import filterfalse, takewhile, count, chain
from math import sqrt,factorial
from modeuler.operators import mul, mod, gt, partial
from modeuler.itertools import unique
from functools import reduce

def divisors(num):
    yield 1
    for i in filterfalse(mod(num),range(2,int(sqrt(num)+1))):
        yield i
        d = num//i
        if d != i:
            yield d
            
def revdivisors(num):
    yield num
    buf = []
    for i in filterfalse(mod(num),(num//i for i in range(2,int(sqrt(num)+1)))):         
        yield i
        d = num//i
        if d != i: buf.append(d)
    for i in buf:
        yield i
    yield 1
    
def pgcd(a,b):
    ia,ib = revdivisors(max(a,b)),revdivisors(min(a,b))
    da,db = next(ia),next(ib)
    while da%db!=0:
        if da > db: da = next(ia)
        else: db = next(ib)
    return db
    
def isprime(n):
    if n<2 or n%2 == 0: return False
    return all(map(mod(n), range(3,int(sqrt(n))+1,2)))

def isprime_sieve(sieve,n):
    modfunc = mod(n)
    limit = gt(int(sqrt(n))+1)
    return all(map(modfunc,takewhile(limit,sieve)))

def aristo(n):
    s = int(sqrt(n))
    return unique(range(2,n),lambda x: map(mul(x),range(2,s)))


SIEVE = [3]
primes = partial(isprime_sieve,SIEVE)

def iterprimes():
    yield 2
    for n in SIEVE:
        yield n
    for n in filter(primes,count(SIEVE[-1]+2,2)):
        yield n
        SIEVE.append(n)

def concat_digit(a,b,n):
    return a*10**n+b

def split_digit(n):
    for c in str(n):
        yield int(c)

def circle_permutations(c):
    d = tuple(chain(c,c[:-1]))
    l = len(c)
    for i in range(l):
        yield d[i:i+l]

def ispal(num):
    s = str(num)
    for i in range(len(s)//2):
        if s[i]!=s[-i-1]: return False
    return True
  
def isbouncy(n):
    it = iter(str(n))
    last = next(it)
    inc = dec = True
    for d in it:
        inc &= d>=last
        dec &= d<=last
        if not(inc or dec): 
            return True
        last = d
    return False

def combi(k,n):
    return factorial(n) // factorial(k) * factorial(n-k)

def prod(it):
    return reduce(mul,it)
