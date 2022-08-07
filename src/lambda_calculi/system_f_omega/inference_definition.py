from lambda_calculi import python_typing as T

from . import kind, type
from .environment import GAMMA, EnvWithTypeVariable
from .inference import And, Inference, ProvesType
from .lib.typography import inline

type_formation: T.Several[Inference] = (
    Inference(
        And(
            (
                ProvesType(GAMMA, type.IsKind(type.TAU1, kind.STAR)),
                ProvesType(GAMMA, type.IsKind(type.TAU2, kind.STAR)),
            )
        ),
        ProvesType(
            GAMMA, type.IsKind(type.Function(type.TAU1, type.TAU2), kind.STAR)
        ),
    ),
    Inference(
        ProvesType(
            EnvWithTypeVariable(GAMMA, type.ALPHA, kind.KAPPA),
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
            EnvWithTypeVariable(GAMMA, type.ALPHA, kind.KAPPA1),
            type.IsKind(type.TAU, kind.KAPPA2),
        ),
        conclusion=ProvesType(
            GAMMA,
            type.IsKind(
                type.TypeFunction(
                    type.IsKind(type.ALPHA, kind.KAPPA1), type.TAU
                ),
                kind.Function(kind.KAPPA1, kind.KAPPA2),
            ),
        ),
    ),
    Inference(
        hypothesis=And(
            (
                ProvesType(
                    GAMMA,
                    type.IsKind(
                        type.TAU1, kind.Function(kind.KAPPA2, kind.KAPPA)
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
        print(inline(section, sep="                   "))


if __name__ == "__main__":
    exit(main())
