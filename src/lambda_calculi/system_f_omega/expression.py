from __future__ import annotations

from dataclasses import dataclass

from .grammar import Grammar
from .kind import Kind
from .lib.variable_base import VariableBase
from .type import Type, TypeVariable


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
    var: Variable
    var_type: Type
    expr: Expression

    def __str__(self):
        return f"λ{self.var}:{self.var_type}.{self.expr}"


@dataclass(frozen=True)
class Application(Expression):
    expr1: Expression
    expr2: Expression

    def __str__(self):
        return f"{self.expr1}{self.expr2}"


@dataclass(frozen=True)
class TypeExpression(Expression):
    type_var: TypeVariable
    var_kind: Kind
    expr: Expression

    def __str__(self):
        return f"Λ{self.type_var}:{self.var_kind}.{self.expr}"


@dataclass(frozen=True)
class TypeApplication(Expression):
    expr: Expression
    type: Type

    def __str__(self):
        return f"{self.expr}{self.type}"
