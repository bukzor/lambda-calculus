"""Generally-useful constructs for python typing."""
import dataclasses
import typing

A = typing.TypeVar("A")
B = typing.TypeVar("B")
Several = tuple[A, ...]
Yields = typing.Generator[A, None, None]
Pairs = Several[tuple[A, B]]
immutable = dataclasses.dataclass(frozen=True)

no_int = typing.cast(int, None)

del dataclasses, typing
