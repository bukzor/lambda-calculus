from lambda_calculi import python_typing as T
from lambda_calculi.system_f_omega.grammar import (
    environment,
    expression,
    kind,
    type,
)
from lambda_calculi.system_f_omega.grammar.environment import GAMMA

from . import (
    And,
    Inference,
    IsAssumed,
    ProvesExpression,
    ProvesType,
    TypeEquivalence,
)

expr = expression

expression_formation: T.Several[Inference] = (
    Inference(
        IsAssumed(expr.HasType(expr.X, type.TAU), GAMMA),
        ProvesExpression(GAMMA, expr.HasType(expr.X, type.TAU)),
    ),
    Inference(
        And(
            (
                ProvesType(GAMMA, type.HasKind(type.TAU1, kind.STAR)),
                ProvesExpression(
                    environment.WithVariable(
                        GAMMA, expr.HasType(expr.X, type.TAU1)
                    ),
                    expr.HasType(expr.E, type.TAU2),
                ),
            )
        ),
        ProvesExpression(
            GAMMA,
            expr.HasType(
                expression.Function(expr.HasType(expr.X, type.TAU1), expr.E),
                type.FunctionType(type.TAU1, type.TAU2),
            ),
        ),
    ),
    Inference(
        And(
            (
                ProvesExpression(
                    GAMMA,
                    expr.HasType(
                        expr.E1, type.FunctionType(type.TAU2, type.TAU)
                    ),
                ),
                ProvesExpression(GAMMA, expr.HasType(expr.E2, type.TAU2)),
            )
        ),
        ProvesExpression(
            GAMMA,
            expr.HasType(expression.Application(expr.E1, expr.E2), type.TAU),
        ),
    ),
    Inference(
        ProvesExpression(
            environment.WithTypeVariable(
                GAMMA, type.HasKind(type.ALPHA, kind.KAPPA)
            ),
            expr.HasType(expr.E, type.TAU),
        ),
        ProvesExpression(
            GAMMA,
            expr.HasType(
                expression.TypeExpression(
                    type.HasKind(type.ALPHA, kind.KAPPA), expr.E
                ),
                type.ForAll(type.HasKind(type.ALPHA, kind.KAPPA), type.TAU),
            ),
        ),
    ),
    Inference(
        And(
            (
                ProvesExpression(
                    GAMMA,
                    expr.HasType(
                        expr.E,
                        type.ForAll(
                            type.HasKind(type.ALPHA, kind.KAPPA), type.TAU
                        ),
                    ),
                ),
                ProvesType(GAMMA, type.HasKind(type.SIGMA, kind.KAPPA)),
            )
        ),
        ProvesExpression(
            GAMMA,
            expr.HasType(
                expression.TypeApplication(expr.E, type.SIGMA),
                type.Substitution(type.TAU, type.ALPHA, type.SIGMA),
            ),
        ),
    ),
    Inference(
        And(
            (
                ProvesExpression(GAMMA, expr.HasType(expr.E, type.TAU)),
                TypeEquivalence(type.TAU, type.SIGMA),
                ProvesType(GAMMA, type.HasKind(type.SIGMA, kind.STAR)),
            )
        ),
        ProvesExpression(GAMMA, expr.HasType(expr.E, type.SIGMA)),
    ),
)


def main():
    for section in ("expression_formation",):
        print("##", section)
        section = globals()[section]

        from ..lib import typography  # pylint:disable=import-outside-toplevel

        print(typography.inline(section, sep="    ", max_width=60))


if __name__ == "__main__":
    exit(main())
