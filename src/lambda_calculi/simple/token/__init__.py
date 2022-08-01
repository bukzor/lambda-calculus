import lambda_calculi.python_typing as T


def pairs_as_kwargs(pairs: T.Pairs[str, object]) -> str:
    return ", ".join([f"{var}={val!r}" for var, val in pairs])


class Token:
    """One token of this language."""

    def __getstate__(self):
        """Must be valid kwargs to __init__."""
        return ()

    def __repr__(self):
        cls = type(self)
        kwargs = pairs_as_kwargs(self.__getstate__())
        return f"{cls.__name__}({kwargs})"
