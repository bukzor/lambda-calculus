from __future__ import annotations

from . import variable


class Grammar:
    pass


class Kind(Grammar):
    STAR: KindVariable
    KAPPA: KindVariable
    KAPPA1: KindVariable
    KAPPA2: KindVariable


class KindVariable(Kind, variable.Variable):
    pass


Kind.STAR = KindVariable("∗")
Kind.KAPPA = KindVariable("κ")
Kind.KAPPA1 = KindVariable("κ", 1)
Kind.KAPPA2 = KindVariable("κ", 2)


class FunctionKind(Kind):
    def __init__(self, kind1: Kind, kind2: Kind):
        self.kind1 = kind1
        self.kind2 = kind2

    def __str__(self):
        return f"{self.kind1} → {self.kind2}"


class Type(Grammar):
    ALPHA: TypeVariable
    BETA: TypeVariable
    SIGMA: TypeVariable
    TAU: TypeVariable
    TAU1: TypeVariable
    TAU2: TypeVariable


class TypeVariable(Type, variable.Variable):
    pass


Type.ALPHA = TypeVariable("α")
Type.BETA = TypeVariable("β")
Type.SIGMA = TypeVariable("σ")
Type.TAU = TypeVariable("τ")
Type.TAU1 = TypeVariable("τ", 1)
Type.TAU2 = TypeVariable("τ", 2)


class FunctionType(Type):
    def __init__(self, type1: Type, type2: Type):
        self.type1 = type1
        self.type2 = type2

    def __str__(self):
        return f"{self.type1} → {self.type2}"


class ForAll(Type):
    def __init__(self, type_var: TypeVariable, var_kind: Kind, type: Type):
        self.type_var = type_var
        self.var_kind = var_kind
        self.type = type

    def __str__(self):
        return f"∀{self.type_var}:{self.var_kind}.{self.type}"


class TypeFunction(Type):
    def __init__(self, type_var: TypeVariable, var_kind: Kind, type: Type):
        self.type_var = type_var
        self.var_kind = var_kind
        self.type = type

    def __str__(self):
        return f"λ{self.type_var}:{self.var_kind}.{self.type}"


class TypeTypeApplication(Type):
    def __init__(self, type1: Type, type2: Type):
        self.type1 = type1
        self.type2 = type2

    def __str__(self):
        return f"{self.type1} {self.type2}"


class Expression(Grammar):
    X: Variable
    E: Variable
    E1: Variable
    E2: Variable


class Variable(Expression, variable.Variable):
    pass


Expression.X = Variable("x")
Expression.E = Variable("e")
Expression.E1 = Variable("e", 1)
Expression.E2 = Variable("e", 2)


class Function(Expression):
    def __init__(self, var: Variable, var_type: Type, expr: Expression):
        self.var = var
        self.var_type = var_type
        self.expr = expr

    def __str__(self):
        return f"λ{self.var}:{self.var_type}.{self.expr}"


class Application(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def __str__(self):
        return f"{self.expr1} {self.expr2}"


class TypeExpression(Expression):
    def __init__(
        self, type_var: TypeVariable, var_kind: Kind, expr: Expression
    ):
        self.type_var = type_var
        self.var_kind = var_kind
        self.expr = expr

    def __str__(self):
        return f"Λ{self.type_var}:{self.var_kind}.{self.expr}"


class TypeApplication(Expression):
    def __init__(self, expr: Expression, type: Type):
        self.expr = expr
        self.type = type

    def __str__(self):
        return f"{self.expr} {self.type}"


class Environment(Grammar):
    GAMMA: EnvVariable
    EMPTY: EnvLiteral


class EnvVariable(Environment, variable.Variable):
    pass


class EnvLiteral(Environment):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


Environment.GAMMA = EnvVariable("Γ")
Environment.EMPTY = EnvLiteral("⟨⟩")


class EnvWithVariable(Environment):
    def __init__(self, env: Environment, var: Variable, type: Type):
        self.env = env
        self.var = var
        self.type = type

    def __str__(self):
        return f"{self.env},({self.var}:{self.type})"


class EnvWithTypeVariable(Environment):
    def __init__(self, env: Environment, type_var: TypeVariable, kind: Kind):
        self.env = env
        self.type_var = type_var
        self.kind = kind

    def __str__(self):
        return f"{self.env},({self.type_var}:{self.kind})"
