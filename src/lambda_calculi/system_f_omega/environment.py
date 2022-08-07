from __future__ import annotations

from dataclasses import dataclass

from .expression import Variable
from .grammar import Grammar
from .kind import Kind
from .lib.variable_base import VariableBase
from .type import Type, TypeVariable


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
class EnvWithVariable(Environment):
    env: Environment
    var: Variable
    type: Type

    def __str__(self):
        return f"{self.env},({self.var}:{self.type})"


@dataclass(frozen=True)
class EnvWithTypeVariable(Environment):
    env: Environment
    type_var: TypeVariable
    kind: Kind

    def __str__(self):
        return f"{self.env},({self.type_var}:{self.kind})"
