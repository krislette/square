
def is_alpha(char: str) -> bool:
    return ('A' <= char <= 'Z') or ('a' <= char <= 'z')

def is_num(char: str) -> bool:
    return '0' <= char <= '9'

def is_space(char: str) -> bool:
    return char == ' '