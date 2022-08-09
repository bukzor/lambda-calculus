from lambda_calculi import python_typing as T
from lambda_calculi.system_f_omega.grammar import environment, kind, type
from lambda_calculi.system_f_omega.grammar.environment import GAMMA

from . import And, Inference, ProvesType

type_formation: T.Several[Inference] = (
    Inference(
        And(
            (
                ProvesType(GAMMA, type.IsKind(type.TAU1, kind.STAR)),
                ProvesType(GAMMA, type.IsKind(type.TAU2, kind.STAR)),
            )
        ),
        ProvesType(
            GAMMA,
            type.IsKind(type.FunctionType(type.TAU1, type.TAU2), kind.STAR),
        ),
    ),
    Inference(
        ProvesType(
            environment.WithTypeVariable(GAMMA, type.ALPHA, kind.KAPPA),
            type.IsKind(type.TAU, kind.STAR),
        ),
        ProvesType(
            GAMMA,
            type.IsKind(
                type.ForAll(type.IsKind(type.ALPHA, kind.KAPPA), type.TAU),
                kind.STAR,
            ),
        ),
    ),
    Inference(
        hypothesis=ProvesType(
            environment.WithTypeVariable(GAMMA, type.ALPHA, kind.KAPPA1),
            type.IsKind(type.TAU, kind.KAPPA2),
        ),
        conclusion=ProvesType(
            GAMMA,
            type.IsKind(
                type.Function(type.IsKind(type.ALPHA, kind.KAPPA1), type.TAU),
                kind.FunctionKind(kind.KAPPA1, kind.KAPPA2),
            ),
        ),
    ),
    Inference(
        hypothesis=And(
            (
                ProvesType(
                    GAMMA,
                    type.IsKind(
                        type.TAU1, kind.FunctionKind(kind.KAPPA2, kind.KAPPA)
                    ),
                ),
                ProvesType(GAMMA, type.IsKind(type.TAU2, kind.KAPPA2)),
            )
        ),
        conclusion=ProvesType(
            GAMMA,
            type.IsKind(type.Application(type.TAU1, type.TAU2), kind.KAPPA),
        ),
    ),
)


def main():
    for section in ("type_formation",):
        print("##", section)
        section = globals()[section]

        from ..lib import typography

        print(typography.inline(section, sep="    ", max_width=50))


if __name__ == "__main__":
    exit(main())
