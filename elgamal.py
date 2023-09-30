from dataclasses import dataclass
from ops import gcde, gen_prime, mod_exp, mod_mult


@dataclass(frozen=True)
class Keys:
    public: int
    private: int


class ElGamal:
    keys: Keys
    generator: int
    mod: int

    def __init__(self, generator: int, mod: int, secret: int) -> None:
        self.generator = generator
        self.mod = mod
        self.keys = ElGamal.generate(generator, mod, secret)

    def encrypt(self, message: int, exp: int = -1) -> tuple[int, int]:
        if exp < 2:
            exp = gen_prime(self.mod, {self.generator})

        v = mod_exp(self.generator, exp, self.mod)
        coef = mod_exp(self.keys.public, exp, self.mod)
        ciphertext = mod_mult(message, coef, self.mod)

        return v, ciphertext

    def decrypt(self, v: int, ciphertext: int) -> int:
        coef = mod_exp(v, self.keys.private, self.mod)
        gcd, coef_inv, _ = gcde(coef, self.mod)
        assert gcd == 1
        message = mod_mult(ciphertext, coef_inv, self.mod)

        return message

    @staticmethod
    def generate(generator: int, mod: int, secret: int = -1) -> Keys:
        if secret < 2:
            secret = gen_prime(mod, {generator})

        public = mod_exp(generator, secret, mod)

        return Keys(public=public, private=secret)
