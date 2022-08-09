from __future__ import annotations

from dataclasses import dataclass

from lambda_calculi import python_typing as T
from lambda_calculi.system_f_omega.grammar import expression, kind, type
from lambda_calculi.system_f_omega.lib.typography import underline

expr = expression


@dataclass(frozen=True)
class Reduction:
    expr1: expr.Expression
    expr2: expr.Expression

    def __str__(self):
        return f"{self.expr1} →→ {self.expr2}"


@dataclass(frozen=True)
class ConditionalReduction(Reduction):
    predicate: Reduction

    def __str__(self):
        hypothesis = str(self.predicate)
        conclusion = super().__str__()
        width = max(len(hypothesis), len(conclusion)) + 4
        return "\n".join(
            (underline(hypothesis.center(width)), conclusion.center(width))
        )


E1_E2 = Reduction(expr.E1, expr.E2)

reduction: T.Several[Reduction] = (
    Reduction(
        expr.Application(
            expr.Function(expr.HasType(expr.X, type.TAU), expr.E), expr.E1
        ),
        expr.Substitution(expr.E, expr.X, expr.E1),
    ),
    Reduction(
        expr.TypeApplication(
            expr.TypeExpression(type.HasKind(type.ALPHA, kind.KAPPA), expr.E),
            type.TAU,
        ),
        expr.TypeSubstitution(expr.E, type.ALPHA, type.TAU),
    ),
    ConditionalReduction(
        expr.Application(expr.E1, expr.E3),
        expr.Application(expr.E2, expr.E3),
        E1_E2,
    ),
    ConditionalReduction(
        expr.Application(expr.E3, expr.E1),
        expr.Application(expr.E3, expr.E2),
        E1_E2,
    ),
    ConditionalReduction(
        expr.TypeApplication(expr.E1, type.TAU),
        expr.TypeApplication(expr.E2, type.TAU),
        E1_E2,
    ),
    ConditionalReduction(
        expr.Function(expr.HasType(expr.X, type.TAU), expr.E1),
        expr.Function(expr.HasType(expr.X, type.TAU), expr.E2),
        E1_E2,
    ),
    ConditionalReduction(
        expr.TypeExpression(type.HasKind(type.ALPHA, kind.KAPPA), expr.E1),
        expr.TypeExpression(type.HasKind(type.ALPHA, kind.KAPPA), expr.E2),
        E1_E2,
    ),
)


def main():
    for section in ("reduction",):
        print("##", section)
        section = globals()[section]

        from .lib import typography  # pylint:disable=import-outside-toplevel

        print(typography.inline(section, sep="    ", max_width=50))


if __name__ == "__main__":
    exit(main())
