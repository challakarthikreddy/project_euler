'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 
'''
# solution 1
rangemax = 20
check_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
     
def find_solution(step):
    for num in xrange(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None
         
if __name__ == '__main__':
    solution = find_solution(20)
    if solution is None:
        print "No answer found "
    else:
        print "found an answer:", solution
# solution 2
    
def delbart(t,n):
    if n > 0:
        if not (t%n):
            if delbart(t, n-1):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

i = 20
while not delbart(i,20):
    i +=20

print i

# solution 3

i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print i

# solution 4
def findsprimes(n):
    primes = [2]
    for i in range(3,n+1):
        for j in primes:
            if(j == primes[len(primes)-1]):
                primes = primes + [i]
            if(i%j == 0):
                break
            else:
                continue
    return primes

def findfactors(n):
    primes = findsprimes(n)
    factors = []
    for i in range(n):
        for j in range(i,n):
            if(i * j == n):
                if(i not in primes):
                    if(j not in primes):
                        factors = findfactors(i) + findfactors(j)
                    else:
                        
                        factors = [j] + findfactors(i)
                    
                else:
                    if( j not in primes):
                        if(i not in primes):
                            factors = findfactors(i) + findfactors(j)
                        else:
                            
                            factors = [i] + findfactors(j)
                    else:
                        factors = [i,j]
                    
                break
    if(n in primes):
        factors = [n]
    return factors
    
def findsmallest(n):
    primes = findsprimes(n)
    primesnum = [0] * len(primes) 
    allzefac = []
    for i in range(n+1):
        allzefac = allzefac + [findfactors(i)]
    for i in primes:
        for j in allzefac:
            if(j.count(i) > primesnum[primes.index(i)]):
                primesnum[primes.index(i)] = j.count(i)
    
    summy = 1
    print primes
    print primesnum
    for i in  range(len(primes)):
        if primesnum[i] != 0:
            summy = summy * primes[i] ** primesnum[i]
    return summy
# solution 5
a = 0
b = 1
for x in range(20):
    a = a + 1
    c = 1
    d = b
    print a,b
    while d % a != 0:
        c = c + 1
        d = b * c
    b = d
# solution 6
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b/gcd(a, b)

print reduce(lcm, range(1, 20+1))

# solution 7
def pfact(n):
    res=[]
    i=2 
    while i < n/2: 
        if n/i == float(n)/i:
            res.append(i)
            n=n/i
        else:
            i+=1
    res.append(n)
    return res

def p5(max_divisor):
    allfacts={}
    for i in range(2,max_divisor+1):
        facts=pfact(i)
        for i in facts:
            allfacts[i]=max(allfacts.get(i,0),facts.count(i))
    d=[item**value for (item,value) in allfacts.items()]
    return reduce(int.__mul__,d)
# solution 8
import math



def primeFactors(n):  #returns list of all prime factors
    primes = primeSieve(int(math.ceil(math.sqrt(n)))+1) 
    factors = list()
    i = 0
    fact = n
    while fact not in primes and i < len(primes):
        if fact%primes[i] == 0:
            fact = fact/primes[i]
            factors.append(primes[i])
        else:
            i+=1
    factors.append(fact) #remaining factor must be prime so add

    uniques = set(factors)
    primeFactorisation = dict()
    for prime in uniques:
        exp = factors.count(prime)        
        primeFactorisation[prime]= exp
    return primeFactorisation




def primeSieve(n):  # returns list of all primes < n
    top =int( math.ceil(math.sqrt(n)))
    poss = set(range(2, n))
    notPrime = set()
    for i in range(2, top, 1):
        if i in notPrime:
            start = 1
        else:
            start = 2
        for j in range(start, n/i+1):
            try:
                notPrime.add(i*j)
            except:
                pass
    primes = list(poss.difference(notPrime))
    primes.sort()
    return primes


def lcm(numList):  # @DuplicatedSignature
    """takes list of numbers, returns lowest common multiple of all numbers"""
    maxExp = dict()
    i = 0
    answer = 1
    for n in numList:
        pFactors = primeFactors(n)
        for factor in pFactors:
            if maxExp.has_key(factor):
                if pFactors[factor] > maxExp[factor]:                    
                    maxExp[factor] = pFactors[factor]
            else:
                maxExp[factor] = pFactors[factor]
        i += 1
        
    for n, e in maxExp.iteritems():
        answer *= pow(n, e)
    
    return answer

lcm(range(1, 21))

# solution 9
def split(n):
    '''
        get all the primitive of n
        2 => [2]
        3 => [3]
        4 => [2,2]
    '''
    
    i = 2
    ret = []
    while(i<=n):
        while(n%i!=0):
            i+=1
        ret.append(i)
        n = n/i
        if(n == 1):
            break
        i = 2
    
    return ret

def convert(primes):
    '''
        count the appearance of each number
        [2] => {2:1}
        [3] => {3:1}
        [2,2] => {2:2}
    '''
    ret = {}
    for i in primes:
        if ret.has_key(i):
            ret[i]+=1
        else:
            ret[i] = 1
    return ret


        
def smallest(n):
    '''
        get the lcm from 1 to n
        for 20 it returns {2: 4, 3: 2, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1}
    '''
    total = {}
    for i in xrange(2, n+1):
        ret = convert(split(i))
        for key in ret.keys():
            if total.has_key(key):
                total[key] = max(total[key], ret[key])
            else:
                total[key] = ret[key]
    return total

def sum(total):
    ret = 1
    for key in total.keys():
        ret *= key**total[key]
    return ret


print sum(smallest(20))

# solution 10

allaprimtal = []
produkt = 1
test = 1
n = 1
upto = 20
while test <= upto:
    if not produkt % test == 0:
        t = test
        for k in allaprimtal:
            while t % k == 0 and t != k and k != 1:
                t //= k
        allaprimtal += [t]
        produkt *= t
    test += 1
print(produkt)


# solution 11

def gcd(a,b):  # @DuplicatedSignature
    while b: a,b = b,a%b
    return a

def lcm(a,b):  # @DuplicatedSignature
    return a*b/gcd(a,b)

def PE(N):
    ans=1
    for i in xrange(2, N+1):
        ans=lcm(i,ans)
    return ans

print PE(20)


# solution 12

from common import primeSieve  # @UnresolvedImport
from math import sqrt, log

def PE(N):  # @DuplicatedSignature
    primes=primeSieve(N+1) #returns list of all primes <=N
    sqrtN=sqrt(N)
    ans=1
    for p in primes:
        if p <= sqrtN:
            ans*=p**(int(log(N)/log(p)))
        else:
            ans*=p
    return ans

print PE(20)

# solution 13
def Problem_5():
    # We just need to multiply the prime factors for all the numbers less than 20
    # Keep in mind that some numbers have the same prime factor multiple times - we need to include all of them in our answer
    # Prime factors: 19, 17, 13, 11, 7, 5, 3, 2
    # 16 = 2 ** 4, so we actually need 4 2's
    # 9 = 3 ** 2, so we need 2 3's
    print 19 * 17 * 13 * 11 * 7 * 5 * 3 * 3 * 2 * 2 * 2 * 2
    
# solution 13 brute forcing

x = 2520

while x > 0:
    for i in range(2, 21):
        if x % i > 0:
            break
        elif i == 20:
            print x
            quit()
    
    x = x + 2520
    
# solution 14 
def smallest_multiple():
    i = 2
    val = True
    while val:
        if i%2==0 and i%3==0 and i%4==0 and i%5==0 and i%6==0 and i%7==0 and i%8==0 and i%9==0 and i%10==0 and i%11==0 and i%12==0 and i%13==0 and i%14==0 and i%15==0 and i%16==0 and i%17==0 and i%18==0 and i%19==0 and i%20==0:         
            return i
        else:
            i += 2
            
# solution 15
def f(x):
    m,i = 1,1
    while i<=x:        
        
        if m%i ==0:
            m *= 1
        else:
            n = 1
            while True:
                if m*n%i == 0:
                    m *=n
                    break
                n +=1
        i+=1
    return m
print f(20)

# solution 16

def euler5(n):
    def pri_fac (n):
        pf = {}
        f = 2
        np = n
        while np > 1:
            while np % f == 0:
                pf[f] = pf.get(f, 0) + 1
                np /= f
            f += ( 1 if f == 2 else 2)
        return pf
     
    nf = {} 
    for i in xrange(2, n+1): 
        pf = pri_fac(i)
        for k in pf:
            if k not in nf:
                nf[k] = pf[k]
            else:
                if nf[k] < pf[k]: nf[k] = pf[k]
    res = 1
    for k,v in nf.iteritems():
        res *= k**v
    return res        

print euler5(20)


# solution 17
divide_max = 20
lst = range(1,divide_max+1)
x = 0
final = 0

while final == 0:
    x += 1
    if all(x%i == 0 for i in lst):
        final = x
        print final
        break

# solution 18

def SM(y,a):
    x=y
    i=1
    while True:
        if x%i==0:
            i=i+1
            if i>a:
                return x
                break
        else:
            x=x+y
            i=1
print (SM((SM(SM(1,5),10)),20))


# solution 19

# Below is my Python code for finding the least common multiple. My is_prime method is pretty basic, and the operate method can use some work, but it did the trick. 

def is_prime(y, z = 2):
    
    """This function determines if a number y is prime
    
    Output: A boolean. True if y is prime. False otherwise. 
    
    Parameter y: We are trying to determine whether or not this number is prime
    Precondition: y is an int greater than 0. 
    
    Parameter z: the number we are dividing y by to determine whether y is prime. Default value is 2
    Precondition: z is an int greater than 0"""
    
    if y < 2:
        return False
    if z == y:
        return True
    else:
        if y%z == 0:
            a = False
        else:
            a = True
    return a and is_prime(y, z+1)

def factorize(n):
    
    """This function will take in a number n and produce a list of its prime factors
    
    Output: a list containing the prime factors of n
    
    Parameter n: the number we are trying to factorize
    Precondition: n is an int greater than or equal to 1"""
    
    if is_prime(n):
        return [n]
    x = (n/2) + 1
    while x >= 2:
        if n%x == 0:
            return factorize(x) + factorize(n/x)
        x -= 1
                
def concatonate(m):
    
    """This function will produce a two dimensional list containing lists of prime factors of numbers from 2 to n.
    
    Output: a two dimensional list containing lists of prime factors of numbers from 2 to n.
    
    Parameter: m is the number until which we will concatenate
    Precondition: m is an int greater than or equal to 1"""
    
    total = []
    for x in range(2, m+1):
        total.append(factorize(x))
    return total
            
def operate(series):
    
    """This function will return the lowest number which is a multiple of concatenated numbers (see concatonate)
    
    Output: the lowest number which is a multiple of concatenated numbers (see concatonate)
    
    Parameter: series is a two dimensional list containing lists of factors of numbers.
    Precondition: series is a two dimensional list"""
    
    number = 1
    for x in series:
        for y in x:
            number *= y
            for z in series:
                if y in z:
                    z.remove(y)
    return number

print operate(concatonate(20))

""" solution 20
    -----------"""
a = 20*19
b = list(range(11,21))
while True:
    for n in b:
        if a%n != 0:
            a += 20
            break
    else:
        print (a)
        break
# solution 21


from time import time

class Divtuple (tuple):
    def __init__(self, t):
        self.t = t
    def __div__(self, n):
        aux = list(self.t)
        for i, x in enumerate(aux):
            if x%n==0: aux[i]=x/n
        return Divtuple(aux)


def lcm(args):  # @DuplicatedSignature
    t = Divtuple(args)
    factors = {2:0,3:0,5:0,7:0,11:0,13:0,17:0,19:0}
    while t != (1,)*len(args):
        for p in (2,3,5,7,11,13,17,19):
            while True:
                aux = t/p
                if aux==t: break
                t = aux
                factors[p]+=1
    v = 1
    for i in factors.keys(): v *= i**factors[i]
    return factors, v

t1 = time()
factors, value = lcm(range(1,20+1))
t2 = time()

facstr = ''
for f in factors.keys():
    if factors[f]>0: facstr += "%d^%d*" % (f,factors[f])
print "FOUND %d = %s" % (value, facstr[:-1])
print "Elapsed %.4f sec" % (t2-t1)


# solution 22
""" 
Since 2520 is the least common multiple of the integers from 1 to 10, 
the least common multiple of the integers from 1 to 20 must be a multiple of 2520. 
By only testing multiples of 2520, the program does not need to confirm divisibility 
by the integers 1 to 10, and instead only confirms divisibility by the integers 11 to 20.

"""
def determineDivisibity(n):
  for divisor in xrange(11, 20):
    if n % divisor != 0:
      return False
  return True

n = 1
while not(determineDivisibity(2520 * n)):
  n += 1
print 2520 * n

