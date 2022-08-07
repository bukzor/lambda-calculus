# from re import compile as Regex

SUBSCRIPT_OFFSET = 0x2080 - 0x30
# ANSI_ESCAPE = Regex("\033[^a-zA-Z]*[a-zA-Z]?")


def subscript(n: int) -> str:
    return "".join(chr(ord(c) + SUBSCRIPT_OFFSET) for c in str(n))


def underline(s: str) -> str:
    return s + "\n" + "-" * len(s)


# def strip_ansi(s: str) -> str:
#    return ANSI_ESCAPE.sub("", s)


def lines_max_width(lines: list[str]) -> int:
    return max((len((line)) for line in lines), default=0)


def inline(
    objs: tuple[object, ...], max_width: int = 79, sep: str = " "
) -> str:
    """Print several objects (possibly containing embedded newlines) inline."""
    lines: list[str] = []
    cursor = 0  # the first non-full line

    for obj in objs:
        new_lines = str(obj).splitlines()

        if cursor < len(lines):
            new_width = max(len(new_line) for new_line in new_lines)

            old_width = lines_max_width(
                lines[cursor : cursor + len(new_lines)]
            )
            if old_width + len(sep) + new_width < max_width:
                lineno = cursor
                for new_line in new_lines:
                    line = lines[lineno] if lineno < len(lines) else ""
                    line = line.ljust(old_width)
                    line = lines[lineno] = (
                        line.ljust(old_width) + sep + new_line
                    )
                    lineno += 1
                continue

        old_lines = lines[cursor:]
        old_width = lines_max_width(old_lines)
        for lineno, line in enumerate(old_lines):
            lines[cursor + lineno] = (
                line.ljust(old_width).center(max_width).rstrip()
            )
        lines.append("")
        lines.append("")
        cursor = len(lines)  # advance to the next blank line
        lines.extend(new_lines)

    old_lines = lines[cursor:]
    old_width = lines_max_width(old_lines)
    for lineno, line in enumerate(old_lines):
        lines[cursor + lineno] = (
            line.ljust(old_width).center(max_width).rstrip()
        )

    return "\n".join(lines)
