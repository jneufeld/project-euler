from common import primes_to_n, get_prime_factors

number = 600851475143
limit = int(number ** 0.5) + 1

primes = primes_to_n(limit)
prime_factors = [prime for prime, _ in get_prime_factors(number, primes)]

print max(prime_factors)
