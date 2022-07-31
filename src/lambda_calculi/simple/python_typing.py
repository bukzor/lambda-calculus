"""Generally-useful constructs for python typing."""
import typing

A = typing.TypeVar("A")
B = typing.TypeVar("B")
Several = tuple[A, ...]
Yields = typing.Generator(T, None, None)
Pairs = Several[Tuple[A, B]]

del typing
