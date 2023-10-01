from __future__ import annotations
from dataclasses import dataclass

from ops import mod_inv

class EllipticCurve:
    a: int
    b: int
    mod: int
    generator: Point

    def __init__(self, a: int, b: int, mod: int, generator: tuple[int, int]) -> None:
        delta = 4 * a * a * a + 27 * b * b
        assert delta != 0
        self.a = a
        self.b = b
        self.mod = mod
        self.generator = Point(*generator, curve=self)

    def add(self, a: int, b: int) -> int:
        return (a + b) % self.mod

    def mult(self, a: int, b: int) -> int:
        return (a * b) % self.mod

    def point(self, x: int, y: int) -> Point:
        return Point(x % self.mod, y % self.mod, self)

    def ith_point(self, i: int) -> Point:
        return self.generator * i

    def eval(self, x: int) -> int:
        return (x * x * x + self.a * x + self.b) % self.mod

    def __contains__(self, point: Point) -> bool:
        return (point.y * point.y) % self.mod == self.eval(point.x)

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    curve: EllipticCurve | None = None

    @staticmethod
    def inf() -> Point:
        return Point(None, None) # type: ignore

    def tuple(self) -> tuple[int, int]:
        return self.x, self.y

    def __neg__(self) -> Point:
        assert self.curve is not None

        return self if self == Point.inf() else Point(self.x, -self.y % self.curve.mod, self.curve)

    def __add__(self, other: Point) -> Point:
        inf: Point = Point.inf()

        if self == inf:
            return other
        elif other == inf:
            return self
        elif self.curve is None or other.curve is None or self == -other:
            return inf
        elif self == other:
            return self._add_self()
        else:
            return self._add_other(other)
            
    def _add_self(self) -> Point:
        assert self.curve is not None

        x1 = (3 * self.x * self.x + self.curve.a) * mod_inv(2 * self.y, self.curve.mod)
        x = x1 * x1 - 2 * self.x
        y = x1 * (self.x - x) - self.y
        
        return Point(x % self.curve.mod, y % self.curve.mod, self.curve)

    def _add_other(self, other: Point) -> Point:
        assert self.curve is not None
        assert self.curve is other.curve

        x1 = (other.y - self.y) * mod_inv(other.x - self.x, self.curve.mod)
        x = x1 * x1 - self.x - other.x
        y = x1 * (self.x - x) - self.y
        
        return Point(x % self.curve.mod, y % self.curve.mod, self.curve)

    def __sub__(self, other: Point) -> Point:
        return self + -other

    def __mul__(self, other: int) -> Point:
        result = Point.inf()

        if self.curve is None:
            return result

        point = -self if other < 0 else self

        while other > 0:
            if (other & 1) == 1:
                result = result + point

            point = point + point
            other >>= 1

        return result

    def __str__(self) -> str:
        return str((self.x, self.y))
