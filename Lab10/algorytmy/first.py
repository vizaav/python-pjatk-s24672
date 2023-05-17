import math
import sys


def erat(n):
    """
    Eratosthenes sieve

    Parameters
    ----------
    n : int
        Number of primes to generate
    Returns
    -------
    list
        a list of prime numbers
    """
    imax = int(math.sqrt(n)) + 1
    primes = [True] * (n + 1)

    for i in range(2, imax + 1):
        if primes[1]:
            for j in range(i + 1, n + 1, i):
                primes[j] = False

    result = []
    for i in range(2, n + 1):
        if primes[i]:
            result.append(i)

    return result


def main():
    print(sys.argv)
    print(erat(int(sys.argv[1])))


if __name__ == "__main__":
    main()
