from . import grammar
from .grammar import Kind, Type, Expression as Expr, Environment as Env
from . import meta_grammar


kinds = meta_grammar.DefinedAs(
    Kind.KAPPA,
    meta_grammar.Or(Kind.STAR, grammar.FunctionKind(Kind.KAPPA1, Kind.KAPPA2)),
)

types = meta_grammar.DefinedAs(
    Type.TAU,
    meta_grammar.Or(
        Type.ALPHA,
        grammar.FunctionType(Type.TAU1, Type.TAU2),
        grammar.ForAll(Type.ALPHA, Kind.KAPPA, Type.TAU),
        grammar.TypeFunction(Type.ALPHA, Kind.KAPPA, Type.TAU),
        grammar.TypeTypeApplication(Type.TAU1, Type.TAU2),
    ),
)

terms = meta_grammar.DefinedAs(
    Expr.E,
    meta_grammar.Or(
        Expr.X,
        grammar.Function(Expr.X, Type.TAU, Expr.E),
        grammar.Application(Expr.E1, Expr.E2),
        grammar.TypeExpression(Type.ALPHA, Kind.KAPPA, Expr.E),
        grammar.TypeApplication(Expr.E, Type.TAU),
    ),
)

environments = meta_grammar.DefinedAs(
    Env.GAMMA,
    meta_grammar.Or(
        Env.EMPTY,
        grammar.EnvWithVariable(Env.GAMMA, Expr.X, Type.TAU),
        grammar.EnvWithTypeVariable(Env.GAMMA, Type.ALPHA, Kind.KAPPA),
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
