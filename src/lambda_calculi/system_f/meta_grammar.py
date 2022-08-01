from . import grammar
from .typography import underline


class MetaGrammar:
    pass


class Nothing(MetaGrammar):
    def __str__(self):
        return ""


class DefinedAs(MetaGrammar):
    def __init__(self, g1: grammar.Grammar, g2: MetaGrammar):
        self.g1 = g1
        self.g2 = g2

    def __str__(self):
        return f"{self.g1} ::= {self.g2}"


class EntailsType(MetaGrammar):
    def __init__(self, env: grammar.Environment, type: grammar.Type):
        self.env = env
        self.type = type

    def __str__(self):
        return f"{self.env}⊢{self.type}"


class EntailsExpression(MetaGrammar):
    def __init__(self, env: grammar.Environment, expr: grammar.Expression):
        self.env = env
        self.expr = expr

    def __str__(self):
        return f"{self.env}⊢{self.expr}"


class And(MetaGrammar):
    def __init__(self, *g: MetaGrammar):
        self.g = g

    def __str__(self):
        g_str = [str(g) for g in self.g]
        width = sum(len(g) for g in g_str) + 5 * (len(g_str) - 1)
        if width < 80:
            return f"{g1str}     {g2str}"
        else:
            return f"{g1str}\n{g2str}"


class Or(MetaGrammar):
    def __init__(self, *g: MetaGrammar):
        self.g = g

    def __str__(self):
        return "|".join(str(g) for g in self.g)


class EvalStep(MetaGrammar):
    def __init__(self, before: MetaGrammar, after: MetaGrammar):
        self.before = before
        self.after = after

    def __str__(self):
        g1str = str(g1)
        g2str = str(g2)
        width = max(len(g1str), len(g2str)) + 2
        return "{underline(g1str.center(width))}\n{g2str.center(width)}"


class TypeEquivalence(MetaGrammar):
    def __init__(self, type1: grammar.Type, type2: grammar.Type):
        self.type1
        self.type2

    def __str__(self):
        return "{self.type1} ≡ {self.type2}"


class TypeVariableSubstitution(MetaGrammar):
    def __init__(
        self,
        type1: grammar.Type,
        type_var: grammar.TypeVariable,
        type2: grammar.Type,
    ):
        self.type1 = type1
        self.type_var = type_var
        self.type2 = type2

    def __str__(self):
        return f"{self.type1}[{self.type_var} := {self.type2}]"


class VariableSubstitution(MetaGrammar):
    def __init__(
        self,
        expr1: grammar.Expression,
        var: grammar.Variable,
        expr2: grammar.Expression,
    ):
        self.expr = expr1
        self.var = var
        self.expr2 = expr2

    def __str__(self):
        return f"{self.expr1}[{self.var1} := {self.expr2}]"


class TypeExpressionSubstitution(MetaGrammar):
    def __init__(
        self,
        expr: grammar.Expression,
        type_var: grammar.TypeVariable,
        type: grammar.Type,
    ):
        self.expr = expr
        self.type_var = type_var
        self.type = type

    def __str__(self):
        return f"{self.expr}[{self.type_var} := {self.type}]"


class Reduction(MetaGrammar):
    def __init__(self, expr1: grammar.Expression, expr2: grammar.Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def __repr__(self):
        return f"{self.expr1} →→ {self.expr2}"
