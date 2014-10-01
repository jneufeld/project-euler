# ==============================================================================
# common.py
#
# Useful algorithms or tools for solving Project Euler questions.
# ==============================================================================

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

import math


# ------------------------------------------------------------------------------
# Utility functions
# ------------------------------------------------------------------------------

def is_prime(number):
    """
    Determine whether number is prime using a brute force approach. Slightly
    optimized to only check odd divisors up to the square root of the number.

    Arguments:
        number<int> -- Number to test.

    Returns:
        True if the number is prime, else false.
    """
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for divisor in xrange(3, int(math.sqrt(number)) + 1, 2):
        if number % divisor == 0:
            return False

    return True


def primes_to_n(limit):
    """
    Find all prime numbers up to the provided limit using the Sieve of Atkin.

    Arguments:
        limit<int> -- Highest value to check primality.

    Returns:
        List of prime numbers less than the given limit.
    """
    if limit < 2:
        return []
    if limit < 5:
        return [2, 3]

    result = []
    result.append(2)
    result.append(3)

    candidates = {}
    for number in xrange(5, limit + 1):
        candidates[number] = False

    for x in xrange(1, int(math.sqrt(limit)) + 1):
        for y in xrange(1, int(math.sqrt(limit)) + 1):
            n = (4 * (x ** 2)) + (y ** 2)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                candidates[n] = not candidates[n]

            n = (3 * (x ** 2)) + (y ** 2)
            if n <= limit and n % 12 == 7:
                candidates[n] = not candidates[n]

            n = (3 * (x ** 2)) - (y ** 2)
            if x > y and n <= limit and n % 12 == 11:
                candidates[n] = not candidates[n]

    for n in xrange(5, int(math.sqrt(limit)) + 1):
        if candidates[n]:
            k, i = n ** 2, 1

            while k <= limit:
                candidates[k] = False
                i += 1
                k = i * (n ** 2)

    for number, prime in candidates.iteritems():
        if prime:
            result.append(number)

    return result


def get_prime_factors(number, primes=[]):
    """
    Finds the prime factors and their multiplicities for a number. If a list of
    primes is supplied, this function does not need to calculate primes. It will
    use the list, saving time.

    Arguments:
        number<int>   -- Number to find prime factors for.
        primes<[int]> -- Optional list of precalculated primes.

    Returns:
        List of tuples, where each tuple contains (prime factor, multiplicity).
    """
    if number < 4:
        return []

    result = []

    possible_prime_factors = []
    n, prime_factors = number, {} 

    if len(primes) == 0:
        possible_prime_factors = primes_to_n((number / 2) + 1)
    else:
        possible_prime_factors = primes[:(number / 2) + 1] 

    for prime in possible_prime_factors:
        while n > 1:
            if n % prime == 0:
                if prime in prime_factors:
                    prime_factors[prime] += 1
                else:
                    prime_factors[prime] = 1

                n /= prime
            else:
                break

    for prime, multiplicity in prime_factors.iteritems():
        result.append((prime, multiplicity))

    return result


def divisor_count(number, primes=[]):
    """
    Find the number of divisors this number has, including 1.

    Arguments:
        number<int>   -- Number which we count divisors for.
        primes<[int]> -- Optional list of precalculated primes.

    Returns:
        Count of divisors the number has, including 1.
    """
    if number < 4:
        return 1

    result = 1

    prime_factors = get_prime_factors(number, primes) 
    for _, multiplicity in prime_factors:
        result *= multiplicity + 1

    result = result if result != 1 else 2

    return result - 1


def get_factors(number):
    """
    Find the factors for the number starting with 1.

    Arguments:
        number<int> -- Number to find divisors for.

    Returns:
        List of integer factors.
    """
    if number < 4:
        return [1]

    result = []

    for divisor in xrange(1, (number / 2) + 1):
        if number % divisor == 0:
            result.append(divisor)

    return result
