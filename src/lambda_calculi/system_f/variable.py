from typing import Optional
from .typography import subscript


class Variable:
    def __init__(self, name: str, subscript: Optional[int] = None):
        self.name = name
        self.subscript = subscript

    def __str__(self):
        result = self.name
        if self.subscript is not None:
            result += subscript(self.subscript)
        return result
