from __future__ import annotations

from dataclasses import dataclass

from lambda_calculi.python_typing import no_int

from .typography import subscript


@dataclass(frozen=True)
class VariableBase:
    name: str
    subscript: int = no_int

    def __str__(self):
        result = self.name
        if self.subscript is not None:
            result += subscript(self.subscript)
        return result
