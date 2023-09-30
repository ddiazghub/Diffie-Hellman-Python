from typing import Callable
from diffie_hellman import diffie_hellman
from attacks import exhaustive_search, baby_step_giant_step
from ops import mod_exp


def attack_test(generator: int, mod: int, exp1: int, exp2: int, attack: Callable[[int, int, int], int]):
    u, v, secret = diffie_hellman(generator, mod, exp1, exp2)
    attack_exp = attack(generator, mod, u)
    attack_secret = mod_exp(v, attack_exp, mod)

    assert secret == attack_secret


def test_exhaustive_search():
    attack_test(3, 17, 15, 13, exhaustive_search)
    attack_test(6, 13, 5, 4, exhaustive_search)
    attack_test(11, 97, 17, 29, exhaustive_search)

def test_baby_step_giant_step():
    attack_test(3, 113, 100, 13, baby_step_giant_step)
    attack_test(3, 17, 15, 13, baby_step_giant_step)
    attack_test(6, 13, 5, 4, baby_step_giant_step)
    attack_test(11, 97, 17, 29, baby_step_giant_step)
