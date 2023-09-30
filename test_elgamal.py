from elgamal import ElGamal
from ops import mod_exp

def test_elgamal():
    generator = 11
    mod = 97
    secret = 17
    cipher = ElGamal(generator, mod, secret)

    assert cipher.keys.public == mod_exp(generator, secret, mod)
    assert cipher.keys.private == secret

    message = 15
    enc_exp = 23
    v, ciphertext = cipher.encrypt(message, enc_exp)

    assert v == 44
    assert ciphertext == 5

    plaintext = cipher.decrypt(v, ciphertext)

    assert plaintext == message
