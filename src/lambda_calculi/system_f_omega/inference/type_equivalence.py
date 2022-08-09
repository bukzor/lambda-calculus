from lambda_calculi import python_typing as T
from lambda_calculi.system_f_omega.grammar import environment, kind, type
from lambda_calculi.system_f_omega.grammar.environment import GAMMA

from . import And, Inference, Nothing, ProvesType, TypeEquivalence

type_equivalence: T.Several[Inference] = (
    Inference(Nothing(), TypeEquivalence(type.TAU, type.TAU)),
    Inference(
        TypeEquivalence(type.TAU, type.SIGMA),
        TypeEquivalence(type.SIGMA, type.TAU),
    ),
    Inference(
        And(
            (
                TypeEquivalence(type.TAU1, type.TAU2),
                TypeEquivalence(type.TAU2, type.TAU3),
            )
        ),
        TypeEquivalence(type.TAU1, type.TAU3),
    ),
    Inference(
        And(
            (
                TypeEquivalence(type.TAU1, type.SIGMA1),
                TypeEquivalence(type.TAU2, type.SIGMA2),
            )
        ),
        TypeEquivalence(
            type.FunctionType(type.TAU1, type.TAU2),
            type.FunctionType(type.SIGMA1, type.SIGMA2),
        ),
    ),
    Inference(
        And((TypeEquivalence(type.TAU, type.SIGMA),)),
        TypeEquivalence(
            type.ForAll(type.IsKind(type.ALPHA, kind.KAPPA), type.TAU),
            type.ForAll(type.IsKind(type.ALPHA, kind.KAPPA), type.SIGMA),
        ),
    ),
    Inference(
        And((TypeEquivalence(type.TAU, type.SIGMA),)),
        TypeEquivalence(
            type.Function(type.IsKind(type.ALPHA, kind.KAPPA), type.TAU),
            type.Function(type.IsKind(type.ALPHA, kind.KAPPA), type.SIGMA),
        ),
    ),
    Inference(
        And(
            (
                TypeEquivalence(type.TAU1, type.SIGMA1),
                TypeEquivalence(type.TAU2, type.SIGMA2),
            )
        ),
        TypeEquivalence(
            type.Application(type.TAU1, type.TAU2),
            type.Application(type.SIGMA1, type.SIGMA2),
        ),
    ),
    Inference(
        Nothing(),
        TypeEquivalence(
            type.Function(type.IsKind(type.ALPHA, kind.KAPPA), type.TAU),
            type.Function(
                type.IsKind(type.BETA, kind.KAPPA),
                type.Substitution(type.TAU, type.ALPHA, type.BETA),
            ),
        ),
    ),
    Inference(
        Nothing(),
        TypeEquivalence(
            type.Application(
                type.Function(type.IsKind(type.ALPHA, kind.KAPPA), type.TAU),
                type.SIGMA,
            ),
            type.Substitution(type.TAU, type.ALPHA, type.SIGMA),
        ),
    ),
)


def main():
    for section in ("type_equivalence",):
        print("##", section)
        section = globals()[section]

        from ..lib import typography

        print(typography.inline(section, sep="    ", max_width=60))


if __name__ == "__main__":
    exit(main())
