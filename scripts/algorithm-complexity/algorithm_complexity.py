import time
import sys

# Set
sys.setrecursionlimit(1000000)

# Rec
def factorial(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    
    return res

def factorial_r(n):
    if n == 1:
        return 1
    else:
        return n * factorial_r(n-1)

if __name__ == '__main__':
    n = 100000
    start = time.time()
    factorial(n)
    end = time.time()
    print(end - start)

    start = time.time()
    factorial_r(n)
    end = time.time()
    print(end - start)