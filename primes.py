"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    number = 2
    found_primes = 1
    primes = [2]

    if number_of_primes <= 0:
        raise ValueError("Please enter a positive number")

    while found_primes < number_of_primes:
        if is_divisible(number, primes):
            primes.append(number)
            found_primes += 1
        number += 1

    return primes


def is_divisible(number, primes):
    composite = True
    for i in primes:
        if number % i == 0:
            composite = False
            break
    return composite
