from __future__ import annotations

from dataclasses import dataclass

from . import Grammar, expression, kind, type
from .lib.variable_base import VariableBase


@dataclass(frozen=True)
class Environment(Grammar):
    pass


@dataclass(frozen=True)
class EnvVariable(Environment, VariableBase):
    pass


@dataclass(frozen=True)
class EnvLiteral(Environment):
    name: str

    def __str__(self):
        return self.name


GAMMA = EnvVariable("Γ")
EMPTY = EnvLiteral("⟨⟩")


@dataclass(frozen=True)
class WithVariable(Environment):
    env: Environment
    has_type: expression.HasType

    def __str__(self):
        return f"{self.env},({self.has_type})"


@dataclass(frozen=True)
class WithTypeVariable(Environment):
    env: Environment
    has_kind: type.HasKind

    def __str__(self):
        return f"{self.env},({self.has_kind})"
