import sys


def fibb(n):
    """
    Fibonacci numbers generator

    Parameters
    ----------
    n : int
        Number of Fibonacci numbers to generate
    Returns
    -------
    number
        a number representing the n-th Fibonacci number
    """
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)


def main():
    print(sys.argv)
    print(fibb(int(sys.argv[1])))


if __name__ == "__main__":
    main()
