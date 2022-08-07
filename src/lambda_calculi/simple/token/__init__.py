import lambda_calculi.python_typing as T


def pairs_as_kwargs(pairs: T.Pairs[str, object]) -> str:
    return ", ".join([f"{var}={val!r}" for var, val in pairs])


@T.immutable
class Token:
    """One token of this language."""
