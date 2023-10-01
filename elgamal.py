from dataclasses import dataclass
from ops import gen_prime, mod_exp, mod_inv, mod_mult
from elliptic_curve import P256, Point


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
        message = mod_mult(ciphertext, mod_inv(coef, self.mod), self.mod)

        return message

    @staticmethod
    def generate(generator: int, mod: int, secret: int = -1) -> Keys:
        if secret < 2:
            secret = gen_prime(mod, {generator})

        public = mod_exp(generator, secret, mod)

        return Keys(public=public, private=secret)


@dataclass(frozen=True)
class KeysP256:
    public: Point
    private: int


class ElGamalP256:
    keys: KeysP256
    _curve: P256

    def __init__(self, secret: int) -> None:
        self._curve = P256()
        self.keys = self.generate(secret)

    def encrypt(self, message: Point, exp: int = -1) -> tuple[Point, Point]:
        if exp < 2:
            exp = gen_prime(P256.Q)

        v = self._curve.generator * exp
        addend = self.keys.public * exp
        ciphertext = message + addend

        return v, ciphertext

    def decrypt(self, v: Point, ciphertext: Point) -> Point:
        minuend = v * self.keys.private

        return ciphertext - minuend

    def generate(self, secret: int = -1) -> KeysP256:
        if secret < 2:
            secret = gen_prime(P256.Q)

        return KeysP256(
            public=self._curve.generator * secret,
            private=secret
        )
