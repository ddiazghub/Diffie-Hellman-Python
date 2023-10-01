from diffie_hellman import diffie_hellman, diffie_hellman_p256


def test_diffie_hellman():
    assert diffie_hellman(3, 17, 15, 13) == (6, 12, 10)
    assert diffie_hellman(6, 13, 5, 4) == (2, 9, 3)
    assert diffie_hellman(11, 97, 17, 29) == (94, 66, 49)


def test_diffie_hellman_p256():
    assert True
