from __future__ import annotations

from dataclasses import dataclass

from lambda_calculi import python_typing as T

from .environment import Environment
from .expression import Expression, Variable
from .grammar import Grammar
from .lib.typography import underline
from .type import Type, TypeVariable


@dataclass(frozen=True)
class Proposition:
    pass


@dataclass(frozen=True)
class Nothing(Proposition):
    def __str__(self):
        return ""


@dataclass(frozen=True)
class IsDefinedAs(Proposition):
    g1: Grammar
    g2: Proposition

    def __str__(self):
        return f"{self.g1} ::= {self.g2}"


@dataclass(frozen=True)
class ProvesType(Proposition):
    env: Environment
    type: Type

    def __str__(self):
        return f"{self.env}⊢{self.type}"


@dataclass(frozen=True)
class ProvesExpression(Proposition):
    env: Environment
    expr: Expression

    def __str__(self):
        return f"{self.env}⊢{self.expr}"


@dataclass(frozen=True)
class And(Proposition):
    g: T.Several[Proposition]

    def __str__(self):
        g_str = [str(g) for g in self.g]
        width = sum(len(g) for g in g_str) + 3 * (len(g_str) - 1)
        if width < 80:
            sep = "   "
        else:
            sep = "\n"
        return sep.join(g_str)


@dataclass(frozen=True)
class Or(Proposition):
    g: T.Several[Grammar]

    def __str__(self):
        return " | ".join(str(g) for g in self.g)


@dataclass(frozen=True)
class Inference(Proposition):
    hypothesis: Proposition
    conclusion: Proposition

    def __str__(self):
        hypothesis = str(self.hypothesis)
        conclusion = str(self.conclusion)
        width = max(len(hypothesis), len(conclusion)) + 4
        return "\n".join(
            (underline(hypothesis.center(width)), conclusion.center(width))
        )


@dataclass(frozen=True)
class TypeEquivalence(Proposition):
    type1: Type
    type2: Type

    def __str__(self):
        return "{self.type1} ≡ {self.type2}"


@dataclass(frozen=True)
class Substitution(Proposition):
    expr1: Expression
    var: Variable
    expr2: Expression

    def __str__(self):
        return f"{self.expr1}[{self.var} := {self.expr2}]"


@dataclass(frozen=True)
class TypeSubstitution(Proposition):
    type1: Type
    type_var: TypeVariable
    type2: Type

    def __str__(self):
        return f"{self.type1}[{self.type_var} := {self.type2}]"


@dataclass(frozen=True)
class TypeExpressionSubstitution(Proposition):
    expr: Expression
    type_var: TypeVariable
    type: Type

    def __str__(self):
        return f"{self.expr}[{self.type_var} := {self.type}]"


@dataclass(frozen=True)
class Reduction(Proposition):
    expr1: Expression
    expr2: Expression

    def __repr__(self):
        return f"{self.expr1} →→ {self.expr2}"
