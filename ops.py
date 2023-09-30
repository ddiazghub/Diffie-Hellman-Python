import secrets


def gcde(r1: int, r2: int) -> tuple[int, int, int]:
    s1, t1 = 1, 0
    s2, t2 = 0, 1

    while r2 != 0:
        q = r1 // r2
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2

    return r1, s1, t1


def mod_mult(a: int, b: int, mod: int) -> int:
    return (a * b) % mod


def mod_exp(n: int, pow: int, mod: int) -> int:
    n = n % mod
    result = 1

    if pow == 0:
        return 1
    elif n == 0:
        return 0

    while pow > 0:
        if (pow & 1) == 1:
            result = mod_mult(result, n, mod)

        pow >>= 1
        n = mod_mult(n, n, mod)

    return result


# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1
def miller_test(n: int, d: int, a: int = -1) -> bool:
    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = a if a > 1 else 2 + secrets.randbelow(n - 2)
    x = mod_exp(a, d, n)

    if x == 1 or x == n - 1:
        return True

    # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while d != n - 1:
        x = (x * x) % n
        d <<= 1

        if x == 1:
            return False
        elif x == n - 1:
            return True

    return False


# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.
def is_prime(n: int, rounds: int = 128) -> bool:
    # Corner cases
    if n <= 1 or n == 4:
        return False

    if n <= 3:
        return True

    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = n - 1

    while d % 2 == 0:
        d //= 2

    # Iterate given number of 'k' times
    for _ in range(rounds):
        if not miller_test(n, d):
            return False

    return True


def randbits(length: int) -> int:
    rand = abs(secrets.randbits(length + 1))

    return rand & ((1 << length) - 1)


def gen_prime(degree: int, exclude: set[int] = set()) -> int:
    while True:
        n = secrets.randbelow(degree)

        if n > 1 and n not in exclude and is_prime(n) :
            return n
