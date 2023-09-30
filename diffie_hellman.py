from ops import gen_prime, mod_exp


def diffie_hellman(generator: int, mod: int, exp1: int = -1, exp2: int = -1) -> tuple[int, int, int]:
    if exp1 < 2 or exp2 < 2:
        exp1 = gen_prime(mod, {generator})
        exp2 = gen_prime(mod, {generator, exp1})

    u = mod_exp(generator, exp1, mod)
    v = mod_exp(generator, exp2, mod)

    shared_secret = mod_exp(v, exp1, mod)
    assert shared_secret == mod_exp(u, exp2, mod)

    return u, v, shared_secret

