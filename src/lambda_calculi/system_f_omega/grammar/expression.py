from __future__ import annotations

from dataclasses import dataclass

from . import Grammar, type
from .lib.variable_base import VariableBase


@dataclass(frozen=True)
class Expression(Grammar):
    pass


@dataclass(frozen=True)
class Variable(Expression, VariableBase):
    pass


X = Variable("x")
E = Variable("e")
E1 = Variable("e", 1)
E2 = Variable("e", 2)


@dataclass(frozen=True)
class Function(Expression):
    has_type: HasType
    expr: Expression

    def __str__(self):
        return f"λ{self.has_type}.{self.expr}"


@dataclass(frozen=True)
class Application(Expression):
    expr1: Expression
    expr2: Expression

    def __str__(self):
        return f"{self.expr1}{self.expr2}"


@dataclass(frozen=True)
class HasType(Expression):
    expr: Expression
    type: type.Type

    def __str__(self):
        return f"{self.expr}:{self.type}"


@dataclass(frozen=True)
class TypeExpression(Expression):
    has_kind: type.HasKind
    expr: Expression

    def __str__(self):
        return f"Λ{self.has_kind}.{self.expr}"


@dataclass(frozen=True)
class TypeApplication(Expression):
    expr: Expression
    type: type.Type

    def __str__(self):
        return f"{self.expr}{self.type}"
