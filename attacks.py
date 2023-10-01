from ops import mod_exp, mod_inv, mod_mult

import math


def exhaustive_search(generator: int, mod: int, target: int) -> int:
    value = 1

    for exp in range(mod + 1):
        if value == target:
            return exp

        value = mod_mult(value, generator, mod)

    return -1


def baby_step_giant_step(generator: int, mod: int, target: int) -> int:
    max = math.ceil(math.sqrt(mod))
    table: dict[int, int] = {}
    value = 1

    for j in range(max):
        table[value] = j
        value = mod_mult(value, generator, mod)

    gen_inv = mod_inv(generator, mod)
    beta = mod_exp(gen_inv, max, mod)
    value = target

    for i in range(max):
        if value in table:
            return i * max + table[value]

        value = mod_mult(value, beta, mod)

    return -1
