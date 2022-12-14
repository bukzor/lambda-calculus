from __future__ import annotations

from dataclasses import dataclass

from . import Grammar
from .kind import Kind
from .lib.variable_base import VariableBase


@dataclass(frozen=True)
class Type(Grammar):
    pass


@dataclass(frozen=True)
class Variable(Type, VariableBase):
    pass


ALPHA = Variable("α")
BETA = Variable("β")
SIGMA = Variable("σ")
SIGMA1 = Variable("σ", 1)
SIGMA2 = Variable("σ", 2)
TAU = Variable("τ")
TAU1 = Variable("τ", 1)
TAU2 = Variable("τ", 2)
TAU3 = Variable("τ", 3)


@dataclass(frozen=True)
class FunctionType(Type):
    type1: Type
    type2: Type

    def __str__(self):
        return f"{self.type1}→{self.type2}"


@dataclass(frozen=True)
class HasKind(Type):
    type: Type
    kind: Kind

    def __str__(self):
        return f"{self.type}:{self.kind}"


@dataclass(frozen=True)
class ForAll(Type):
    has_kind: HasKind
    type: Type

    def __str__(self):
        return f"∀{self.has_kind}.{self.type}"


@dataclass(frozen=True)
class Function(Type):
    has_kind: HasKind
    type: Type

    def __str__(self):
        return f"λ{self.has_kind}.{self.type}"


@dataclass(frozen=True)
class Application(Type):
    type1: Type
    type2: Type

    def __str__(self):
        return f"{self.type1}{self.type2}"


@dataclass(frozen=True)
class Substitution(Type):
    type: Type
    var1: Variable
    var2: Variable

    def __str__(self):
        return f"{self.type}[{self.var1}:={self.var2}]"
