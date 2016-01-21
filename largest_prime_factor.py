"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? 
"""

class Largest_prime_factors():
    def largest_prime_factor(self,n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
                print i
            else:
                n //= i
                print n
        print n

if __name__ == '__main__':
    test = Largest_prime_factors()
    test.largest_prime_factor(68)