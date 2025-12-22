def sqrt(x):
    return x**0.5

def sin(x):
    return math.sin(math.radians(x))

def pow(base, exp):
    return base ** exp

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a