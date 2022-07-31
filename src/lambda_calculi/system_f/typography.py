SUBSCRIPT_OFFSET = 0x2080 - 0x30

def subscript(n: int) -> str:
    return ''.join(
        chr(ord(c) + SUBSCRIPT_OFFSET)
        for c in str(n)
    )

def underline(s: str) -> str:
    combining_character_low_line = '\u0332'
    return ''.join(c + combining_character_low_line for c in s)
