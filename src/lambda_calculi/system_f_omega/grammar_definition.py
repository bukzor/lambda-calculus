from . import inference
from .grammar import environment, expression, kind, type

kinds = inference.IsDefinedAs(
    kind.KAPPA,
    inference.Or((kind.STAR, kind.FunctionKind(kind.KAPPA1, kind.KAPPA2))),
)

types = inference.IsDefinedAs(
    type.TAU,
    inference.Or(
        (
            type.ALPHA,
            type.FunctionType(type.TAU1, type.TAU2),
            type.ForAll(type.HasKind(type.ALPHA, kind.KAPPA), type.TAU),
            type.Function(type.HasKind(type.ALPHA, kind.KAPPA), type.TAU),
            type.Application(type.TAU1, type.TAU2),
        )
    ),
)

terms = inference.IsDefinedAs(
    expression.E,
    inference.Or(
        (
            expression.X,
            expression.Function(
                expression.HasType(expression.X, type.TAU), expression.E
            ),
            expression.Application(expression.E1, expression.E2),
            expression.TypeExpression(
                type.HasKind(type.ALPHA, kind.KAPPA), expression.E
            ),
            expression.TypeApplication(expression.E, type.TAU),
        )
    ),
)

environments = inference.IsDefinedAs(
    environment.GAMMA,
    inference.Or(
        (
            environment.EMPTY,
            environment.WithVariable(
                environment.GAMMA, expression.HasType(expression.X, type.TAU)
            ),
            environment.WithTypeVariable(
                environment.GAMMA, type.HasKind(type.ALPHA, kind.KAPPA)
            ),
        )
    ),
)


def main():
    print("```")
    for x in ("kinds", "types", "terms", "environments"):
        print(f"({x})", end=" ")
        print(globals()[x])
    print("```")


if __name__ == "__main__":
    exit(main())
