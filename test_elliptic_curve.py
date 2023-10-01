from elliptic_curves import EllipticCurve, Point


def test_addition():
    # Example curve parameters
    a, b = 4, 20
    generator = (2, 6)
    mod = 29
    curve = EllipticCurve(a, b, mod, generator)

    # Example points on the curve
    p = curve.point(1, 5)
    q = curve.point(20, 3)

    # Test point addition
    assert p + p == curve.point(4, 19)  # 1P + 1P = 2P
    assert p + q == curve.point(15, 27)  # 1P + Q = R

    # Additional test cases
    r = curve.point(15, 27)
    s = curve.point(6, 12)
    u = curve.point(20, 26)

    assert p + Point.inf() == p  # P + O = P (where O is the point at infinity)
    assert p - p == p + -p and p - p == Point.inf()  # P + (-P) = O
    assert p + r == s  # P + R = S
    assert r + p == s  # R + P = S
    assert r + u == p  # R + U = P


def test_multiplication():
    # Example curve parameters
    a, b = 0, 7
    generator = (15, 13)
    mod = 17
    curve = EllipticCurve(a, b, mod, generator)

    # Expected values from generator
    expected = [
        (None, None),
        (15, 13),
        (2, 10),
        (8, 3),
        (12, 1),
        (6, 6),
        (5, 8),
        (10, 15),
        (1, 12),
        (3, 0),
        (1, 5),
        (10, 2),
        (5, 9),
        (6, 11),
        (12, 16),
        (8, 14),
        (2, 7),
        (15, 4),
        (None, None),
        (15, 13),
        (2, 10),
        (8, 3),
        (12, 1),
        (6, 6),
        (5, 8),
    ]

    for i, point in enumerate(expected):
        assert curve.ith_point(i).tuple() == point
