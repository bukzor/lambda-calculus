"""Generally-useful constructs for python typing."""
import typing

A = typing.TypeVar("A")
B = typing.TypeVar("B")
Several = tuple[A, ...]
Yields = typing.Generator[A, None, None]
Pairs = Several[tuple[A, B]]

del typing
