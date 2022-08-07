from dataclasses import dataclass

from . import Token


@dataclass(frozen=True)
class Expression(Token):  # called "term" in the literature
    pass


@dataclass(frozen=True)
class Variable(Expression):
    name: str

    def __str__(self):
        return self.name


@dataclass(frozen=True)
class Application(Expression):
    expression1: Expression
    expression2: Expression

    def __str__(self):
        return f"{self.expression1} {self.expression2}"


@dataclass(frozen=True)
class Abstraction(Expression):
    variable: Variable
    expression: Expression

    def __str__(self):
        return f"λ{self.variable}.{self.expression}"
