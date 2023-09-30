from ops import mod_exp, randbits


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


def test_randbits():
    for _ in range(10000):
        rand = randbits(32)
        assert rand > 0 and rand < (1 << 32)
