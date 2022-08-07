from . import environment, expression, inference, kind, type

kinds = inference.IsDefinedAs(
    kind.KAPPA,
    inference.Or((kind.STAR, kind.Function(kind.KAPPA1, kind.KAPPA2))),
)

types = inference.IsDefinedAs(
    type.TAU,
    inference.Or(
        (
            type.ALPHA,
            type.Function(type.TAU1, type.TAU2),
            type.ForAll(type.IsKind(type.ALPHA, kind.KAPPA), type.TAU),
            type.TypeFunction(type.IsKind(type.ALPHA, kind.KAPPA), type.TAU),
            type.Application(type.TAU1, type.TAU2),
        )
    ),
)

terms = inference.IsDefinedAs(
    expression.E,
    inference.Or(
        (
            expression.X,
            expression.Function(expression.X, type.TAU, expression.E),
            expression.Application(expression.E1, expression.E2),
            expression.TypeExpression(type.ALPHA, kind.KAPPA, expression.E),
            expression.TypeApplication(expression.E, type.TAU),
        )
    ),
)

environments = inference.IsDefinedAs(
    environment.GAMMA,
    inference.Or(
        (
            environment.EMPTY,
            environment.EnvWithVariable(
                environment.GAMMA, expression.X, type.TAU
            ),
            environment.EnvWithTypeVariable(
                environment.GAMMA, type.ALPHA, kind.KAPPA
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
