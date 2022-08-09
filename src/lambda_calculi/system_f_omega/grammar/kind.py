from __future__ import annotations

from dataclasses import dataclass

from . import Grammar
from .lib.variable_base import VariableBase


@dataclass(frozen=True)
class Kind(Grammar):
    pass


@dataclass(frozen=True)
class KindVariable(Kind, VariableBase):
    pass


STAR = KindVariable("⚹")
KAPPA = KindVariable("κ")
KAPPA1 = KindVariable("κ", 1)
KAPPA2 = KindVariable("κ", 2)


@dataclass(frozen=True)
class FunctionKind(Kind):
    kind1: Kind
    kind2: Kind

    def __str__(self):
        return f"{self.kind1}→{self.kind2}"
