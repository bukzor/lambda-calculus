from lambda_calculi.simple.token import expression


def test_it_can_catch_typeerrors():
    bad_token = expression.Variable(name=123)  # E: Argument of type "Literal[123]" cannot be assigned to parameter "name" of type "str" in function "__init__"
    reveal_type(bad_token)  # T: Variable
    assert not bad_token


def test_it_notices_explicit_type_error():
    myint: int = "3"  # E: Expression of type "Literal['3']" cannot be assigned to declared type "int"
    del myint
