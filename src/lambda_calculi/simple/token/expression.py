"""According to https://plato.stanford.edu/entries/lambda-calculus/"""
from . import Token

class Term(Token):
    pass

class Variable(Term):
    def __str__(self):
        return self.name

    def __init__(name: str):
        self.name = name

    def __repr__(self):
        cls = type(self)
        return f'{cls.__name__}(name={self.name!r})'

def Application(Term):
    def __init__(e1: Term, e2: Term):
        self.e1 = e1
        self.e2 = e2

    return __str__(self):
        return f'{self.e1} {self.e2}'

def Abstraction(Term):
    def __init__(self, 


