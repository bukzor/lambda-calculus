from .typography import subscript

class Variable:
    def __init__(self, name: str, subscript: int = None):
        self.name = name
        self.subscript = subscript
    def __str__(self):
        result = self.name
        if self.subscript is not None:
            result += subscript(str(self.subscript))
        return result
