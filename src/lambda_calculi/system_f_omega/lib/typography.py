SUBSCRIPT_OFFSET = 0x2080 - 0x30


def subscript(n: int) -> str:
    return "".join(chr(ord(c) + SUBSCRIPT_OFFSET) for c in str(n))


def underline(s: str) -> str:
    return f"[4m{s}[0m"
