from elgamal import ElGamal, ElGamalP256
from elliptic_curve import P256
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

def test_elgamal_p256():
    secret = 17
    cipher = ElGamalP256(secret)
    gen = cipher._curve.generator

    assert cipher.keys.public == gen * secret
    assert cipher.keys.private == secret

    message = gen * 5
    enc_exp = 23
    v, ciphertext = cipher.encrypt(message, enc_exp)

    assert v == gen * enc_exp
    assert ciphertext != message

    plaintext = cipher.decrypt(v, ciphertext)
    
    assert plaintext == message
