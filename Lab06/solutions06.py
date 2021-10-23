def recursive_fib(n):
    # base case if 1, return 1
    if n <= 1:
        return n
    else:
        # fib(n) = fib(n-1) + fib(n-2)
        return(recursive_fib(n-1) + recursive_fib(n-2))

def checkForPrime(n, i = 2):
    # base case
    if (n < 2):
        return False
    if n==2:
        return True
    if (n % i == 0):
        return False
    if (i * i > n):
        return True

    # Check for next divisor
    return checkForPrime(n, i + 1)


def q01():
    """Write a function that calculates the 𝑛!"
    Fibonacci number without using any type of
    loop"""
    n = int(input("Please enter the fibonacci number you want to see: "))
    for i in range(n+1):
        print(f"{i}: {recursive_fib(i)}")


def q02():
    """Write a function that determine if a number is
    a prime number without using any type of
    loop."""
    n = int(input("Please enter the number you want to check is a Prime: "))
    for i in range(n+1):
        print(f"{i}: Prime? {checkForPrime(i)}")

q02()

