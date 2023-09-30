from ops import gcd, gcde, mod_exp, is_prime, randbits


def test_gcd():
    assert gcd(7, 11) == 1
    assert gcd(8, 8) == 8
    assert gcd(10, 0) == 10
    assert gcd(16, 20) == 4
    assert gcd(36, 48) == 12
    assert gcd(17, 19) == 1
    assert gcd(0, 0) == 0
    assert gcd(987654321, 12345) == 3
    assert gcd(999999937, 999999929) == 1
    assert gcd(1234567890, 987654321) == 9
    assert gcd(999999999989, 999999999979) == 1
    assert gcd(999999999990, 999999999980) == 10
    assert gcd(987654321234567890, 1234567890987654321) == 1
    assert gcd(1234567890, 0) == 1234567890
    assert gcd(0, 1234567890) == 1234567890
    assert gcd(999999999989, 999999999991) == 1
    assert gcd(999999937, 0) == 999999937
    assert gcd(0, 999999937) == 999999937
    assert gcd(999999937, 1) == 1
    assert gcd(1, 999999937) == 1
    assert (
        gcd(123456789012345678901234567890, 98765432109876543210987654321)
        == 900000000090000000009
    )
    assert (
        gcd(999999999999999999999999999999, 999999999999999999999999999999)
        == 999999999999999999999999999999
    )


def test_gcde():
    assert gcde(30, 20) == (10, 1, -1)
    assert gcde(35, 15) == (5, 1, -2)

    # Test case 1: GCD of two prime numbers
    a, b = 17, 19
    gcd, x, y = gcde(a, b)
    assert gcd == 1
    assert a * x + b * y == gcd

    # Test case 2: GCD of two identical numbers
    a, b = 8, 8
    gcd, x, y = gcde(a, b)
    assert gcd == 8
    assert a * x + b * y == gcd

    # Test case 3: GCD of two consecutive numbers
    a, b = 12, 13
    gcd, x, y = gcde(a, b)
    assert gcd == 1
    assert a * x + b * y == gcd

    # Test case 4: GCD of two numbers with a common divisor
    a, b = 36, 48
    gcd, x, y = gcde(a, b)
    assert gcd == 12
    assert a * x + b * y == gcd

    # Test case 5: GCD of two numbers with no common divisor other than 1
    a, b = 25, 49
    gcd, x, y = gcde(a, b)
    assert gcd == 1
    assert a * x + b * y == gcd

    # Test case 6: GCD of two large numbers
    a, b = 12345, 67890
    gcd, x, y = gcde(a, b)
    assert gcd == 15
    assert a * x + b * y == gcd

    # Test case 7: GCD of two large prime numbers
    a, b = 999999937, 999999929
    gcd, x, y = gcde(a, b)
    assert gcd == 1
    assert a * x + b * y == gcd

    # Test case 8: GCD of two large numbers with a common divisor
    a, b = 987654321, 123456789
    gcd, x, y = gcde(a, b)
    assert gcd == 9
    assert a * x + b * y == gcd


def test_mod_exp():
    # Test case 1: Basic modular exponentiation with small numbers
    result = mod_exp(2, 3, 5)
    assert result == 3  # 2^3 % 5 = 8 % 5 = 3

    # Test case 2: Modular exponentiation with a large exponent
    result = mod_exp(7, 1000, 13)
    assert result == 9  # (7^1000) % 13 = 9

    # Test case 3: Modular exponentiation with a large base and exponent
    result = mod_exp(123456789, 987654321, 1000000007)
    assert result == 652541198  # (123456789^987654321) % 1000000007

    # Test case 4: Modular exponentiation with a large modulus
    result = mod_exp(3, 5000, 1000000007)
    assert result == 22443616  # (3^5000) % 1000000007

    # Test case 5: Modular exponentiation with a base of 1
    result = mod_exp(1, 999, 17)
    assert result == 1  # 1^999 % 17 = 1

    # Test case 6: Modular exponentiation with a base of 0
    result = mod_exp(0, 12345, 100000007)
    assert result == 0  # 0^12345 % 100000007 = 0

    # Test case 7: Modular exponentiation with a modulus of 1
    result = mod_exp(12345, 999, 1)
    assert result == 0  # 12345^999 % 1 = 0

    # Test case 8: Modular exponentiation with a base and exponent of 0
    result = mod_exp(0, 0, 100000007)
    assert result == 1  # 0^0 % 100000007 = 1

    # Test case 9: Modular exponentiation with a small modulus
    result = mod_exp(10, 20, 7)
    assert result == 2  # (10^20) % 7 = 100000000000000000000 % 7 = 2

    # Test case 10: Modular exponentiation with a prime modulus
    result = mod_exp(17, 42, 23)
    assert (
        result == 16
    )  # (17^42) % 23 = 4773695331839566234818968439734627784374274207965089 % 23 = 16


def test_is_prime():
    # Test case 1: Prime number
    assert is_prime(2)

    # Test case 2: Prime number
    assert is_prime(13)

    # Test case 3: Prime number
    assert is_prime(97)

    # Test case 4: Prime number
    assert is_prime(101)

    # Test case 5: Non-prime number (even)
    assert not is_prime(4)

    # Test case 6: Non-prime number (even)
    assert not is_prime(100)

    # Test case 7: Non-prime number (composite)
    assert not is_prime(15)

    # Test case 8: Non-prime number (composite)
    assert not is_prime(1000)

    # Test case 9: Non-prime number (small composite)
    assert not is_prime(1)

    # Test case 10: Non-prime number (small composite)
    assert not is_prime(0)

    # Test case 11: Non-prime number (negative)
    assert not is_prime(-7)

    # Test case 12: Non-prime number (negative)
    assert not is_prime(-11)

    # Test case 13: Prime number (large prime)
    assert is_prime(999999937)

    # Test case 14: Non-prime number (large non-prime)
    assert not is_prime(999999938)

    # Test case 15: Non-prime number (large non-prime)
    assert not is_prime(999999941)


def test_randbits():
    for _ in range(10000):
        rand = randbits(32)
        assert rand > 0 and rand < (1 << 32)
