def get_unique_text(input: str) -> str:
    return "".join(i + '\u200B' for i in input)