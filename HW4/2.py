"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

# Без использования «Решета Эратосфена»;
import re


def isPrime(n):
    # see http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None


N = int(input("N: ")) # number of primes wanted (from command-line)
M = 100              # upper-bound of search space
l = list()           # result list

while len(l) < N:
    l += filter(isPrime, range(M - 100, M)) # append prime element of [M - 100, M] to l
    M += 100                                # increment upper-bound

print (l[:N]) # print result list limited to N elements


"""
# Используя алгоритм «Решето Эратосфена»
primes = [2, 3]
last_crossed = [2, 3]


def add_next_prime():
    candidate = primes[-1] + 2
    i = 0
    while i < len(primes):
        while last_crossed[i] < candidate:
            last_crossed[i] += primes[i]
        if last_crossed[i] == candidate:
            candidate += 2
            i = 0
        i += 1

    primes.append(candidate)
    last_crossed.append(candidate)


def fill_primes(n):
    while len(primes) < n:
        add_next_prime()


fill_primes(10)
print(primes)
"""